package mapper;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import dto.HeadHunterResponse;
import dto.Vacancy;

import java.util.List;

public class HeadHunterResponseMapper {
    private final ObjectMapper objectMapper;

    public HeadHunterResponseMapper() {
        this.objectMapper = new ObjectMapper();
    }

    public List<Vacancy> map(String json) {
        try {
            HeadHunterResponse response = objectMapper.readValue(json, HeadHunterResponse.class);

            return response.items().stream()
                    .map(item -> new Vacancy(
                            item.id(),
                            item.name(),
                            item.employer() != null
                                    ? item.employer().name()
                                    : null,
                            item.salary() != null
                                    ? item.salary().from()
                                    : null,
                            item.salary() != null
                                    ? item.salary().to()
                                    : null,
                            item.salary() != null
                                    ? item.salary().currency()
                                    : null,
                            item.alternateUrl()
                    ))
                    .toList();
        } catch (JsonProcessingException e) {
            System.out.println("JSON parsing error:");
            e.printStackTrace();
            System.out.println("Received JSON:");
            System.out.println(json);

            throw new RuntimeException("Failed to parse HeadHunter response", e);
        }
    }
}
