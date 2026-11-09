package com.kstu.weather_bridge.dto.response.api;

import com.fasterxml.jackson.annotation.JsonProperty;

public record OpenMeteoResponse(
    Current current
) {
    public record Current(
            @JsonProperty("temperature_2m")
            double temperature,

            @JsonProperty("relative_humidity_2m")
            double humidity,

            @JsonProperty("weather_code")
            int weatherCode,

            @JsonProperty("wind_speed_10m")
            double windSpeed,

            @JsonProperty("surface_pressure")
            double atmosphericPressure
    ) {
    }
}
