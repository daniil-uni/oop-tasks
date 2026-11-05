package creators;

import styles.WidgetStyle;
import widget.Widget;

public class LabelCreator extends WidgetCreator {
    public LabelCreator(WidgetStyle style) {
        super(style);
    }

    @Override
    public Widget create(String text) {
        System.out.println(text);
        Widget widget = new Widget("Label");
        style.apply(widget);
        return widget;
    }
}
