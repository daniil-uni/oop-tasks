package com.kstu.weather_bridge.provider;

import com.kstu.weather_bridge.client.ApiClient;
import com.kstu.weather_bridge.dto.WeatherData;
import com.kstu.weather_bridge.dto.response.api.MetNorwayResponse;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.web.util.UriComponentsBuilder;

import java.net.URI;
import java.time.Duration;
import java.time.Instant;
import java.util.Comparator;

@Component
public class MetNorwayProvider implements WeatherProvider {
    private static final double LATITUDE = 49.806;
    private static final double LONGITUDE = 73.085;

    private static final String USER_AGENT =
            "WeatherBridge/1.0 (mailto:tkacevnikita8@gmail.com)";

    private final ApiClient client;

    public MetNorwayProvider(@Qualifier("metNorwayApiClient") ApiClient client) {
        this.client = client;
    }

    @Override
    public WeatherData getWeatherData(String city) {
        MetNorwayResponse response = client.get(
                buildWeatherUri(),
                MetNorwayResponse.class,
                "User-Agent",
                USER_AGENT
        );

        MetNorwayResponse.TimePoint timePoint =
                findClosestTimePoint(response);

        MetNorwayResponse.Details details =
                timePoint.data().instant().details();

        return WeatherData.builder()
                .city(city)
                .temperatureInCelsius(details.temperature())
                .description(getWeatherDescription(timePoint))
                .humidity(details.humidity())
                .windSpeed(details.windSpeed())
                .atmosphericPressure(details.atmosphericPressure())
                .build();
    }

    private URI buildWeatherUri() {
        return UriComponentsBuilder
                .fromUriString(
                        "https://api.met.no/weatherapi/locationforecast/2.0/compact"
                )
                .queryParam("lat", LATITUDE)
                .queryParam("lon", LONGITUDE)
                .build()
                .encode()
                .toUri();
    }

    private MetNorwayResponse.TimePoint findClosestTimePoint(
            MetNorwayResponse response
    ) {
        Instant now = Instant.now();

        return response.properties()
                .timeseries()
                .stream()
                .min(Comparator.comparingLong(point ->
                        Math.abs(Duration.between(
                                now,
                                Instant.parse(point.time())
                        ).toMillis())
                ))
                .orElseThrow(() ->
                        new IllegalStateException("Weather forecast is empty")
                );
    }

    private String getWeatherDescription(MetNorwayResponse.TimePoint timePoint) {
        MetNorwayResponse.Data data = timePoint.data();

        MetNorwayResponse.Period period = data.next1Hours();

        if (period == null) {
            period = data.next6Hours();
        }

        if (period == null) {
            period = data.next12Hours();
        }

        if (period == null || period.summary() == null) {
            return "Неизвестные погодные условия";
        }

        String symbolCode = period.summary().symbolCode();

        if (symbolCode == null) {
            return "Неизвестные погодные условия";
        }

        return switch (symbolCode.replaceFirst("_(day|night|polartwilight)$", "")) {
            case "clearsky" -> "Ясно";
            case "fair" -> "Преимущественно ясно";
            case "partlycloudy" -> "Переменная облачность";
            case "cloudy" -> "Облачно";
            case "fog" -> "Туман";
            case "lightrain" -> "Небольшой дождь";
            case "rain" -> "Дождь";
            case "heavyrain" -> "Сильный дождь";
            case "lightsnow" -> "Небольшой снег";
            case "snow" -> "Снег";
            case "heavysnow" -> "Сильный снегопад";
            case "sleet" -> "Дождь со снегом";
            default -> "Неизвестные погодные условия";
        };
    }
}
