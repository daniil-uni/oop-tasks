package widget;

public class Widget {
    private String typeName;
    private String styleDescription;

    public Widget(String typeName) {
        this.typeName = typeName;
    }

    public void setStyleDescription(String styleDescription) {
        this.styleDescription = styleDescription;
    }

    public void display() {
        System.out.println(typeName + " " + styleDescription);
    }
}
