package styles;

import widget.Widget;

public class DarkStyle extends WidgetStyle {
    @Override
    public void apply(Widget widget) {
        widget.setStyleDescription("dark colour");
    }
}
