from django.contrib import admin
from .page.models import Page
from .widget.models import Widget

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'route')
    search_fields = ('title', 'route')
    filter_horizontal = ('widgets',)

@admin.register(Widget)
class WidgetAdmin(admin.ModelAdmin):
    change_form_template = 'widgets/widget_admin.html'

    class Media:
        js = ('dynamic_pages/js/admin_widget.js',)

    # def change_view(self, request, object_id, form_url="", extra_context=None):
    #     extra_context = extra_context or {}
    #     extra_context['widget_types'] = Widget.WIDGET_TYPES
    #     return super().change_view(request, object_id, form_url, extra_context=extra_context)
    # list_display = ('type', 'config')
