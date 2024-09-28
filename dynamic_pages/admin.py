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
    list_display = ('type', 'config')
