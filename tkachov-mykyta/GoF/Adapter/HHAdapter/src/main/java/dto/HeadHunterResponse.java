package dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.List;

@JsonIgnoreProperties(ignoreUnknown = true)
public record HeadHunterResponse(
        List<HeadHunterVacancy> items
) {
    @JsonIgnoreProperties(ignoreUnknown = true)
    public record HeadHunterVacancy(
            String id,
            String name,
            Employer employer,
            Salary salary,

            @JsonProperty("alternate_url")
            String alternateUrl
    ) {}

    @JsonIgnoreProperties(ignoreUnknown = true)
    public record Employer(
            String name
    ) {}

    @JsonIgnoreProperties(ignoreUnknown = true)
    public record Salary(
            Integer from,
            Integer to,
            String currency
    ) {}
}
