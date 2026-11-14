package service;

import dto.Vacancy;

import java.util.List;

public interface VacancyService {
    List<Vacancy> search(String keyword);
}