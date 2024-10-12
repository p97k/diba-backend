from dynamic_pages.widget.widget_views.base import BaseWidgetView


class ImageView(BaseWidgetView):
    def get_data(self, config):
        result = {
            'image_url': config['image']['image_url'],
        }

        return result