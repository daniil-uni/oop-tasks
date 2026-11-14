import client.HeadHunterClient;
import mapper.HeadHunterResponseMapper;
import service.HeadHunterAdapter;
import service.VacancyService;

void main() {
    VacancyService service = new HeadHunterAdapter(
            new HeadHunterClient(),
            new HeadHunterResponseMapper()
    );

    service.search("Java")
            .forEach(IO::println);
}