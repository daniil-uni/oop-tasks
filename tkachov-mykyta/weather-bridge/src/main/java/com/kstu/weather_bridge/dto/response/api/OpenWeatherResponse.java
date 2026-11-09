package com.kstu.weather_bridge.dto.response.api;

import java.util.List;

public record OpenWeatherResponse(
        List<Weather> weather,
        Main main,
        Wind wind,
        String name
) {
    public record Weather(String description) {}

    public record Main(
            double temp,
            double pressure,
            double humidity
    ) {}

    public record Wind(double speed) {}
}
