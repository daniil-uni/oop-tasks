package com.kstu.weather_bridge.factory;

import com.kstu.weather_bridge.bridge.DetailedWeatherView;
import com.kstu.weather_bridge.bridge.ShortWeatherView;
import com.kstu.weather_bridge.bridge.WeatherView;
import com.kstu.weather_bridge.enums.WeatherSource;
import com.kstu.weather_bridge.enums.WeatherViewType;
import com.kstu.weather_bridge.mapper.WeatherResponseMapper;
import com.kstu.weather_bridge.provider.WeatherProvider;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

@Component
public class WeatherViewFactory {
    private final WeatherProvider openMeteoProvider;
    private final WeatherProvider openWeatherProvider;
    private final WeatherResponseMapper responseMapper;

    public WeatherViewFactory(
            @Qualifier("openMeteoProvider") WeatherProvider openMeteoProvider,
            @Qualifier("openWeatherProvider") WeatherProvider openWeatherProvider,
            WeatherResponseMapper responseMapper
    ) {
        this.openMeteoProvider = openMeteoProvider;
        this.openWeatherProvider = openWeatherProvider;
        this.responseMapper = responseMapper;
    }

    public WeatherView create(
            WeatherSource source,
            WeatherViewType viewType
    ) {
        WeatherProvider provider = switch (source) {
            case OPEN_METEO -> openMeteoProvider;
            case OPEN_WEATHER -> openWeatherProvider;
        };

        return switch (viewType) {
            case SHORT -> new ShortWeatherView(provider, responseMapper);
            case DETAILED -> new DetailedWeatherView(provider, responseMapper);
        };
    }
}
