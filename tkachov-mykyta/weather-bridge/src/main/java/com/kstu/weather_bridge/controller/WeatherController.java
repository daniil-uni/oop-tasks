package com.kstu.weather_bridge.controller;

import com.kstu.weather_bridge.dto.response.WeatherResponse;
import com.kstu.weather_bridge.enums.WeatherSource;
import com.kstu.weather_bridge.enums.WeatherViewType;
import com.kstu.weather_bridge.factory.WeatherViewFactory;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/weather")
@RequiredArgsConstructor
public class WeatherController {
    private final WeatherViewFactory viewFactory;

    @GetMapping
    public ResponseEntity<WeatherResponse> getWeather(
            @RequestParam(value = "source", defaultValue = "OPEN_METEO") WeatherSource source,
            @RequestParam(value = "view", defaultValue = "SHORT") WeatherViewType viewType,
            @RequestParam String city
            ) {
        return ResponseEntity.ok(viewFactory.create(source, viewType).getWeatherInfo(city));
    }
}
