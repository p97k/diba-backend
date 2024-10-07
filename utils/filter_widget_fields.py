from functools import wraps

def filter_widget_fields(fields_to_save):
    """Decorator to filter widget fields when saving."""
    def decorator(func):
        @wraps(func)
        def wrapper(self, request, obj, form, change):
            new_config = {}

            for field in fields_to_save:
                if field in request.POST:
                    new_config[field] = request.POST.get(field)

            if obj.config is None:
                obj.config = {}

            obj.config[self.widget_type] = new_config

            return func(self, request, obj, form, change)
        return wrapper
    return decorator
