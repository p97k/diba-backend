from .base import BaseWidgetView

class PostWidgetView(BaseWidgetView):
    def get_data(self, config):
        result = {
            'title': config['post']['title'],
            'description': config['post']['description'],
            'image_url': config['post']['image_url'],
        }

        return result