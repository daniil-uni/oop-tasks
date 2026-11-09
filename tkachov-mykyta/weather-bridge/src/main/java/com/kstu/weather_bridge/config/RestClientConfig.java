package com.kstu.weather_bridge.config;

import com.kstu.weather_bridge.client.ApiClient;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestClient;

@Configuration
public class RestClientConfig {
    @Bean
    public RestClient openMeteoRestClient() {
        return RestClient.builder()
                .baseUrl("https://api.open-meteo.com")
                .build();
    }

    @Bean
    public RestClient openWeatherRestClient() {
        return RestClient.builder()
                .baseUrl("https://api.openweathermap.org")
                .build();
    }

    @Bean
    public ApiClient openMeteoApiClient(
            @Qualifier("openMeteoRestClient") RestClient restClient) {
        return new ApiClient(restClient);
    }

    @Bean
    public ApiClient openWeatherApiClient(
            @Qualifier("openWeatherRestClient") RestClient restClient) {
        return new ApiClient(restClient);
    }
}
