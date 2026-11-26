public class StatisticsDisplay implements Observer {
	private final double[] values;

	public StatisticsDisplay() {
		values = new double[];
	}

	@Override
	public void update(double temperature, int humidity) {
		values.add(temperature);

		IO.println("Statistic: min " + min() + ", max: " + max() + ", avg: " + avg());
	}

	private double avg() {
		return sum() / values.length;
	}

	private double sum() {
		double sumOfTemperatures = 0;
		
		for (double temp : values) {
			sumOfTemperatures += temp;
		}

		return sumOfTemperatures;
	}

	private double min() {
		double minTemp = values[0];

		for (double temp : values) {
			if (temp < minTemp) {
				minTemp = temp;
			}
		}

		return minTemp;
	}

	private double max() {
		double maxTemp = values[0];

		for (double temp : values) {
			if (temp > maxTemp) {
				maxTemp = temp;
			}
		}

		return maxTemp;
	}
}