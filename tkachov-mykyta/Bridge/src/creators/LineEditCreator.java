package creators;

import styles.WidgetStyle;
import widget.Widget;

public class LineEditCreator extends WidgetCreator {
    public LineEditCreator(WidgetStyle style) {
        super(style);
    }

    @Override
    public Widget create(String text) {
        System.out.println(text);
        Widget widget = new Widget("Line Edit");
        style.apply(widget);
        return widget;
    }
}
