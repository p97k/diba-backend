from django.contrib import admin
from .page.models import Page
from .widget.models import Widget

from .widget.widget_factory import WidgetHandlerFactory


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'route')
    search_fields = ('title', 'route')
    filter_horizontal = ('widgets',)

@admin.register(Widget)
class WidgetAdmin(admin.ModelAdmin):
    list_display = ('type', 'config')
    search_fields = ('type',)
    exclude = ('config',)
    change_form_template = 'admin/dynamic_pages/widget/change_form.html'

    def get_form(self, request, obj=None, **kwargs):
        widget_type = obj.type if obj else "post"
        handler = WidgetHandlerFactory.get_handler(widget_type)
        return handler.get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        widget_type = form.cleaned_data.get('type')
        handler = WidgetHandlerFactory.get_handler(widget_type)
        handler.save_model(request, obj, form, change)
        super().save_model(request, obj, form, change)
