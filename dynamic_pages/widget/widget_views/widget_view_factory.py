from dynamic_pages.widget.widget_views.image_view import ImageView
from dynamic_pages.widget.widget_views.post_view import PostWidgetView

class WidgetViewFactory:
    @staticmethod
    def get_view(widget_type):
        if widget_type == 'post':
            return PostWidgetView()
        if widget_type == 'image':
            return ImageView()
        else:
            raise ValueError(f"Unknown widget type: {widget_type}")