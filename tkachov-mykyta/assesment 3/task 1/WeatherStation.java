class WeatherStation extends Subject {
	public static double temperature;
	public static int humidity;

	public WeatherStation() {
		super();
	}

	public void set_measurements(double temperature, int humidity) {
		if (this.temperature != temperature || this.humidity != humidity) {
			this.temperature = temperature;
			this.humidity = humidity;

			notify(temperature, humidity);
		}	
	}
}