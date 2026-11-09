package com.kstu.weather_bridge.client;

import lombok.RequiredArgsConstructor;
import org.springframework.web.client.RestClient;

import java.net.URI;

@RequiredArgsConstructor
public class ApiClient {
    private final RestClient restClient;

    public <T> T get(URI uri, Class<T> responseType) {
        return restClient.get()
                .uri(uri)
                .retrieve()
                .body(responseType);
    }
}
