package com.kstu.weather_bridge.bridge;

import com.kstu.weather_bridge.dto.WeatherData;
import com.kstu.weather_bridge.dto.response.WeatherResponse;
import com.kstu.weather_bridge.mapper.WeatherResponseMapper;
import com.kstu.weather_bridge.provider.WeatherProvider;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor(access = AccessLevel.PROTECTED)
public abstract class WeatherView {
    private final WeatherProvider weatherProvider;
    protected final WeatherResponseMapper responseMapper;

    public abstract WeatherResponse getWeatherInfo(String city);

    protected WeatherData getWeatherDataFromProvider(String city) {
        return weatherProvider.getWeatherData(city);
    }
}
