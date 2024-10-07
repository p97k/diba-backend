from .widget_handlers.image_handler import ImageWidgetHandler
from .widget_handlers.post_handler import PostWidgetHandler

class WidgetHandlerFactory:
    @staticmethod
    def get_handler(widget_type):
        if widget_type == 'post':
            return PostWidgetHandler()
        if widget_type == 'image':
            return ImageWidgetHandler()
        else:
            raise ValueError(f"Unknown widget type: {widget_type}")
