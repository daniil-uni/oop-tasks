package com.kstu.weather_bridge.dto.response;

public record ShortWeatherResponse(
        String city,
        double temperature,
        String description
) implements WeatherResponse {
}
