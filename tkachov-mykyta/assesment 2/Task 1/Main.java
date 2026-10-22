class Main {
	public static void main(String[] args) {
		Warehouse warehouse = new Warehouse();
		warehouse.addItem("Hat");
		warehouse.addItem("Coat");
		
		System.out.println(warehouse.getItemQuantity());
	}
}