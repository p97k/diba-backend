class BaseWidgetView:
    def get_data(self, config):
        raise NotImplementedError("Subclasses must implement get_data")

    def handle_widget_data(self, data):
        result = {
            'id': data['id'],
            'type': data['type'],
            'config': self.get_data(data['config']),
        }

        return result