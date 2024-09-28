from rest_framework import serializers
from .models import Page
from ..widget.serializers import WidgetSerializer

class PageSerializer(serializers.ModelSerializer):
    widgets = WidgetSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ['id', 'title', 'route', 'widgets']
