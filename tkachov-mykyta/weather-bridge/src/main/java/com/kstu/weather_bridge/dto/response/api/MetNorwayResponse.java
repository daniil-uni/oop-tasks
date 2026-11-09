package com.kstu.weather_bridge.dto.response.api;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.List;

public record MetNorwayResponse(Properties properties) {

    public record Properties(List<TimePoint> timeseries) {}

    public record TimePoint(
            String time,
            Data data
    ) {}

    public record Data(
            InstantData instant,

            @JsonProperty("next_1_hours")
            Period next1Hours,

            @JsonProperty("next_6_hours")
            Period next6Hours,

            @JsonProperty("next_12_hours")
            Period next12Hours
    ) {}

    public record InstantData(Details details) {}

    public record Details(
            @JsonProperty("air_temperature")
            double temperature,

            @JsonProperty("relative_humidity")
            double humidity,

            @JsonProperty("wind_speed")
            double windSpeed,

            @JsonProperty("air_pressure_at_sea_level")
            double atmosphericPressure
    ) {}

    public record Period(Summary summary) {}

    public record Summary(
            @JsonProperty("symbol_code")
            String symbolCode
    ) {}
}
