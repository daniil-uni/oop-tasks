
import requests
from abc import ABC, abstractmethod
from urllib.parse import quote


# Интерфейс погодного API
class WeatherAPI(ABC):

    @abstractmethod
    def get_weather(self, city):
        pass


# Первое API
class OpenMeteoAPI(WeatherAPI):

    def get_weather(self, city):
        # Получаем координаты города
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_response = requests.get(
            geo_url,
            params={"name": city, "count": 1, "language": "ru"}
        )
        geo_data = geo_response.json()

        if not geo_data.get("results"):
            raise Exception("Город не найден")

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]

        # Получаем погоду по координатам
        weather_url = "https://api.open-meteo.com/v1/forecast"

        response = requests.get(
            weather_url,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m,weather_code"
            }
        )

        data = response.json()
        current = data["current"]

        weather_codes = {
            0: "Ясно",
            1: "Преимущественно ясно",
            2: "Переменная облачность",
            3: "Пасмурно",
            45: "Туман",
            48: "Изморозь",
            51: "Лёгкая морось",
            53: "Морось",
            55: "Сильная морось",
            61: "Небольшой дождь",
            63: "Дождь",
            65: "Сильный дождь",
            71: "Небольшой снег",
            73: "Снег",
            75: "Сильный снег",
            95: "Гроза"
        }

        return {
            "city": city_name,
            "temperature": current["temperature_2m"],
            "feels_like": current["apparent_temperature"],
            "humidity": current["relative_humidity_2m"],
            "wind": current["wind_speed_10m"],
            "description": weather_codes.get(
                current["weather_code"], "Неизвестно"
            )
        }


class WttrAPI(WeatherAPI):

    def get_weather(self, city):
        url = f"https://wttr.in/{quote(city)}"

        response = requests.get(
            url,
            params={"format": "j1"},
            headers={"User-Agent": "Mozilla/5.0"}
        )

        data = response.json()
        current = data["current_condition"][0]

        return {
            "city": city,
            "temperature": float(current["temp_C"]),
            "feels_like": float(current["FeelsLikeC"]),
            "humidity": int(current["humidity"]),
            "wind": float(current["windspeedKmph"]),
            "description": current["weatherDesc"][0]["value"]
        }


# Абстракция отображения погоды
class WeatherDisplay(ABC):

    def __init__(self, api):
        self.api = api

    @abstractmethod
    def show_weather(self, city):
        pass


class SimpleDisplay(WeatherDisplay):

    def show_weather(self, city):
        weather = self.api.get_weather(city)

        print("\n--- Погода ---")
        print("Город:", weather["city"])
        print("Температура:", weather["temperature"], "°C")
        print("Описание:", weather["description"])


class DetailedDisplay(WeatherDisplay):

    def show_weather(self, city):
        weather = self.api.get_weather(city)

        print("\n--- Подробная погода ---")
        print("Город:", weather["city"])
        print("Температура:", weather["temperature"], "°C")
        print("Ощущается как:", weather["feels_like"], "°C")
        print("Влажность:", weather["humidity"], "%")
        print("Скорость ветра:", weather["wind"], "км/ч")
        print("Описание:", weather["description"])


def main():

    print("=== ПОГОДНОЕ ПРИЛОЖЕНИЕ ===")

    city = input("Введите город: ")

    print("\nВыберите погодное API:")
    print("1. Open-Meteo")
    print("2. wttr.in")

    api_choice = input("Ваш выбор: ")

    if api_choice == "1":
        api = OpenMeteoAPI()
    elif api_choice == "2":
        api = WttrAPI()
    else:
        print("Неверный выбор API")
        return

    print("\nВыберите способ отображения:")
    print("1. Краткий")
    print("2. Подробный")

    display_choice = input("Ваш выбор: ")

    if display_choice == "1":
        display = SimpleDisplay(api)
    elif display_choice == "2":
        display = DetailedDisplay(api)
    else:
        print("Неверный способ отображения")
        return

    try:
        display.show_weather(city)
    except Exception as error:
        print("Ошибка получения погоды:", error)


if __name__ == "__main__":
    main()
