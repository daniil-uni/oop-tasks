package com.kstu.weather_bridge.dto;

import lombok.Builder;

@Builder
public record WeatherData(
        String city,
        double temperatureInCelsius,
        String description,
        double humidity,
        double windSpeed,
        double atmosphericPressure
) {
}
