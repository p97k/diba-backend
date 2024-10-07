from django.contrib import admin
from .page.models import Page
from .widget.models import Widget
from django import forms

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

    def get_form(self, request, obj=None, **kwargs):
        widget_type = obj.type if obj else request.POST.get('type', None)
        handler = WidgetHandlerFactory.get_handler(widget_type)
        return handler.get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        widget_type = obj.type if obj else request.POST.get('type', None)
        handler = WidgetHandlerFactory.get_handler(widget_type)
        handler.save_model(request, obj, form, change)

