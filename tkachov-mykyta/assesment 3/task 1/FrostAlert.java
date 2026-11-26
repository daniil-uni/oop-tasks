public class FrostAlert implemets Observer {
	@Override
	public void update(double temperature, int humidity) {
		if (temperature < 0) {
			IO.println("Caution! Low temperature!");
		}
	}
}