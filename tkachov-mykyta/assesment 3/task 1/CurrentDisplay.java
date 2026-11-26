public class CurrentDisplay implements Observer {
	@Override
	public void update(double temperature, int humidity) {
		IO.println("Now: " + temperature + "C, humidity: " + humidity + "%");
	}
}