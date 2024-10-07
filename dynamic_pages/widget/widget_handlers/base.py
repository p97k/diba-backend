class BaseWidgetHandler:
    form_class = None

    def get_form(self, request, obj=None, **kwargs):
        raise NotImplementedError("Subclasses must implement get_form")

    def save_model(self, request, obj, form, change):
        raise NotImplementedError("Subclasses must implement save_model")
