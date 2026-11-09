package com.kstu.weather_bridge.dto.response;

public record DetailedWeatherResponse(
        String city,
        double temperature,
        String description,
        double humidity,
        double windSpeed,
        double atmosphericPressure
) implements WeatherResponse {
}
