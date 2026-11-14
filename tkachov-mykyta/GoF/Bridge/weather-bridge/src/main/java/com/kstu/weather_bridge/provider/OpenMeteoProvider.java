package com.kstu.weather_bridge.provider;

import com.kstu.weather_bridge.client.ApiClient;
import com.kstu.weather_bridge.dto.WeatherData;
import com.kstu.weather_bridge.dto.response.api.OpenMeteoResponse;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;
import org.springframework.web.util.UriComponentsBuilder;

import java.net.URI;

@Component
public class OpenMeteoProvider implements WeatherProvider {
    private static final double LATITUDE = 49.806;
    private static final double LONGITUDE = 73.085;

    @Qualifier("openMeteoApiClient")
    private final ApiClient client;

    public OpenMeteoProvider(
            @Qualifier("openMeteoApiClient") ApiClient client) {
        this.client = client;
    }

    @Override
    public WeatherData getWeatherData(String city) {
        OpenMeteoResponse.Current response = client.get(buildWeatherURI(), OpenMeteoResponse.class).current();

        return WeatherData.builder()
                .city(city)
                .temperatureInCelsius(response.temperature())
                .description(getWeatherDescription(response.weatherCode()))
                .humidity(response.humidity())
                .windSpeed(response.windSpeed())
                .atmosphericPressure(response.atmosphericPressure())
                .build();
    }

    private URI buildWeatherURI() {
        return UriComponentsBuilder
                .fromUriString("https://api.open-meteo.com/v1/forecast")
                .queryParam("latitude", LATITUDE)
                .queryParam("longitude", LONGITUDE)
                .queryParam("current", String.join(",",
                        "temperature_2m",
                        "relative_humidity_2m",
                        "weather_code",
                        "wind_speed_10m",
                        "surface_pressure"
                ))
                .queryParam("wind_speed_unit", "ms")
                .build()
                .encode()
                .toUri();
    }

    private String getWeatherDescription(int weatherCode) {
        return switch (weatherCode) {
            case 0 -> "Ясно";

            case 1 -> "Преимущественно ясно";
            case 2 -> "Переменная облачность";
            case 3 -> "Пасмурно";

            case 45, 48 -> "Туман";

            case 51, 53, 55 -> "Морось";
            case 56, 57 -> "Ледяная морось";

            case 61, 63, 65 -> "Дождь";
            case 66, 67 -> "Ледяной дождь";

            case 71, 73, 75 -> "Снегопад";
            case 77 -> "Снежные зёрна";

            case 80, 81, 82 -> "Ливень";
            case 85, 86 -> "Снегопад (ливневый)";

            case 95 -> "Гроза";
            case 96, 99 -> "Гроза с градом";

            default -> "Неизвестные погодные условия";
        };
    }
}
