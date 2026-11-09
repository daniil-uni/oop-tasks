package com.kstu.weather_bridge.provider;

import com.kstu.weather_bridge.dto.WeatherData;

public interface WeatherProvider {
    WeatherData getWeatherData(String city);
}
