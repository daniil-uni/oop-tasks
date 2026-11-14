package dto;

public record Vacancy(
        String id,
        String title,
        String company,
        Integer salaryFrom,
        Integer salaryTo,
        String currency,
        String url
) {
}
