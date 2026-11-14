package com.kstu.weather_bridge.mapper;

import com.kstu.weather_bridge.dto.WeatherData;
import com.kstu.weather_bridge.dto.response.DetailedWeatherResponse;
import com.kstu.weather_bridge.dto.response.ShortWeatherResponse;
import org.mapstruct.Mapper;
import org.mapstruct.Mapping;

@Mapper(componentModel = "spring")
public interface WeatherResponseMapper {
    @Mapping(target = "temperature", source = "temperatureInCelsius")
    ShortWeatherResponse toShortResponse(WeatherData weatherData);

    @Mapping(target = "temperature", source = "temperatureInCelsius")
    DetailedWeatherResponse toDetailedResponse(WeatherData weatherData);
}
