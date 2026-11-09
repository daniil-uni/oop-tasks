package com.kstu.weather_bridge.provider;

import com.kstu.weather_bridge.client.ApiClient;
import com.kstu.weather_bridge.dto.WeatherData;
import com.kstu.weather_bridge.dto.response.api.OpenWeatherResponse;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.web.util.UriComponentsBuilder;

import java.net.URI;

@Component
public class OpenWeatherProvider implements WeatherProvider {
    private final ApiClient client;
    private final String apiKey;

    public OpenWeatherProvider(
            @Qualifier("openWeatherApiClient") ApiClient client,
            @Value("${openweather.api-key}") String apiKey
    ) {
        this.client = client;
        this.apiKey = apiKey;
    }

    @Override
    public WeatherData getWeatherData(String city) {
        OpenWeatherResponse response = client.get(buildWeatherUri(city), OpenWeatherResponse.class);

        return WeatherData.builder()
                .city(response.name())
                .temperatureInCelsius(response.main().temp())
                .description(response.weather().getFirst().description())
                .humidity(response.main().humidity())
                .windSpeed(response.wind().speed())
                .atmosphericPressure(response.main().pressure())
                .build();
    }

    private URI buildWeatherUri(String city) {
        return UriComponentsBuilder
                .fromUriString("https://api.openweathermap.org/data/2.5/weather")
                .queryParam("q", city)
                .queryParam("appid", apiKey)
                .queryParam("units", "metric")
                .queryParam("lang", "ru")
                .build()
                .encode()
                .toUri();
    }
}
