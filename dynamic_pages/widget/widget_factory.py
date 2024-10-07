from .widget_handlers.post_handler import PostWidgetHandler

class WidgetHandlerFactory:
    @staticmethod
    def get_handler(widget_type):
        if widget_type == 'post':
            return PostWidgetHandler()
        else:
            raise ValueError(f"Unknown widget type: {widget_type}")
