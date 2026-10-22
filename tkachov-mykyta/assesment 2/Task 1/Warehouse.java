import java.util.List;
import java.util.ArrayList;

class Warehouse {
	private List<Item> items;

	public Warehouse() {
		items = new ArrayList<>();
	}

	private class Item {
		private final String name;

		private Item(String name) {
			this.name = name;
		}

		public String getName() {
			return name;
		}
	}

	public void addItem(String name) {
		items.add(new Item(name));
	}

	public int getItemQuantity() {
		return items.size();
	} 	
}