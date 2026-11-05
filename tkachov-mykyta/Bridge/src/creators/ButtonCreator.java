package creators;

import styles.WidgetStyle;
import widget.Widget;

public class ButtonCreator extends WidgetCreator {
    public ButtonCreator(WidgetStyle style) {
        super(style);
    }

    @Override
    public Widget create(String text) {
        System.out.println(text);
        Widget widget = new Widget("Button");
        style.apply(widget);
        return widget;
    }
}
