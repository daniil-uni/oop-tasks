class CurrentDisplay:
    def update(self, temperature: float, humidity: int):
        print(f'Сейчас: {temperature} °C, влажность {humidity}%')


class StatisticsDisplay:
    def __init__(self):
        self.values = []

    def update(self, temperature: float, humidity: int):
        self.values.append(temperature)
        avg = sum(self.values) / len(self.values)
        print(f'Статистика: мин {min(self.values)}, макс {max(self.values)}, среднее {avg:.1f}')

class FrostAlert:
    def update(self, temperature: float, humidity: int):
        if temperature < 0:
            print('Внимание! Возможен мороз!')

#___________________________________________________________________________________

class Subject:
    def __init__(self):
        self.nablyudateli = []

    def attach(self, observer):
        if observer not in self.nablyudateli:
            self.nablyudateli.append(observer)

    def detach(self, observer):
        if observer in self.nablyudateli:
            self.nablyudateli.remove(observer)

    def notify(self, *args):
        for nabludatel in self.nablyudateli:
            nabludatel.update(*args)


class WeatherStation(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.temperatura = None
        self.vlazhnost = None

    def set_measurements(self, temperature, humidity):
        if temperature != self.temperatura or humidity != self.vlazhnost:
            self.temperatura = temperature
            self.vlazhnost = humidity
            self.notify(temperature, humidity)


if __name__ == '__main__':
    station = WeatherStation()
    current, stats, alert = CurrentDisplay(), StatisticsDisplay(), FrostAlert()
    for d in (current, stats, alert, current):
        station.attach(d)
    station.set_measurements(5, 70)
    station.set_measurements(5, 70)
    station.detach(stats)
    station.set_measurements(-2, 80)