import creators.ButtonCreator;
import creators.LabelCreator;
import creators.WidgetCreator;
import styles.DarkStyle;
import styles.GreenStyle;
import styles.WidgetStyle;
import widget.Widget;

public class Main {
    public static void main(String[] args) {
        WidgetStyle greenStyle = new GreenStyle();
        WidgetCreator buttonCreator = new ButtonCreator(greenStyle);

        Widget button = buttonCreator.create("Creating button");

        WidgetStyle darkStyle = new DarkStyle();
        WidgetCreator labelCreator = new LabelCreator(darkStyle);

        Widget label = labelCreator.create("Creating label");
        label.display();
    }
}
