package com.kstu.weather_bridge.bridge;

import com.kstu.weather_bridge.dto.response.WeatherResponse;
import com.kstu.weather_bridge.mapper.WeatherResponseMapper;
import com.kstu.weather_bridge.provider.WeatherProvider;
import org.springframework.stereotype.Component;

public class DetailedWeatherView extends WeatherView {
    public DetailedWeatherView(WeatherProvider weatherProvider, WeatherResponseMapper responseMapper) {
        super(weatherProvider, responseMapper);
    }

    @Override
    public WeatherResponse getWeatherInfo(String city) {
        return responseMapper.toDetailedResponse(super.getWeatherDataFromProvider(city));
    }
}
