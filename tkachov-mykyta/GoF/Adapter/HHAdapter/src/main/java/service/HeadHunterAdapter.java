package service;

import client.HeadHunterClient;
import dto.Vacancy;
import mapper.HeadHunterResponseMapper;

import java.util.List;

public class HeadHunterAdapter implements VacancyService {
    private static final int REQUEST_LIMIT = 7;

    private final HeadHunterClient client;
    private final HeadHunterResponseMapper mapper;

    public HeadHunterAdapter(HeadHunterClient client, HeadHunterResponseMapper mapper) {
        this.client = client;
        this.mapper = mapper;
    }

    @Override
    public List<Vacancy> search(String keyword) {
        String vacanciesResponse;

        try {
            vacanciesResponse = client.fetchVacancies(keyword, REQUEST_LIMIT);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        return mapper.map(vacanciesResponse);
    }
}
