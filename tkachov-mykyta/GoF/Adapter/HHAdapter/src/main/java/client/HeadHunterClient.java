package client;

import config.HeadHunterConfig;

import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;

public class HeadHunterClient {
    private static final String BASE_URL = HeadHunterConfig.get("hh.api.base-url");
    private static final String TOKEN = HeadHunterConfig.get("hh.api.token");
    private static final String USER_AGENT = HeadHunterConfig.get("hh.api.user-agent");

    private final HttpClient client = HttpClient.newHttpClient();

    public String fetchVacancies(String query, int limit) throws Exception {

        String encoded = URLEncoder.encode(query, StandardCharsets.UTF_8);

        String url = BASE_URL
                + "/vacancies?text=" + encoded
                + "&per_page=" + limit
                + "&host=hh.kz";

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("HH-User-Agent", USER_AGENT)
                .header("Authorization", "Bearer " + TOKEN)
                .GET()
                .build();

        HttpResponse<String> response =
                client.send(
                        request,
                        HttpResponse.BodyHandlers.ofString()
                );

        if (response.statusCode() != 200) {
            throw new RuntimeException(
                    "HH API error: " + response.statusCode()
            );
        }

        return response.body();
    }

}
