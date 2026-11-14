package creators;

import styles.WidgetStyle;
import widget.Widget;

public abstract class WidgetCreator {
    protected WidgetStyle style;

    public WidgetCreator(WidgetStyle style) {
        this.style = style;
    }

    public abstract Widget create(String text);
}
