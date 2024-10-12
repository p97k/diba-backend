from dynamic_pages.widget.widget_views.post_view import PostWidgetView

class WidgetViewFactory:
    @staticmethod
    def get_view(widget_type):
        if widget_type == 'post':
            return PostWidgetView()
        else:
            raise ValueError(f"Unknown widget type: {widget_type}")