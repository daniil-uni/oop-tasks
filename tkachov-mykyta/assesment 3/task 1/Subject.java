import java.util.*;

abstract class Subject {
	private List<Observer> observers;

	protected Subject() {
		observers = new ArrayList();
	}
	
	public void attach(Observer observer) {
		if (!observers.contains(observer)) {
			observers.add(observer);
		}
	}

	public void detach(Observer observer) {
		if (observers.contains(observer)) {
			observers.remove(observer);
		}
	}


	protected void notify(double temperature, int humidity) {
		for (Observer observer : observers) {
			observer.update(temperature, humidity);
		}
	}
}