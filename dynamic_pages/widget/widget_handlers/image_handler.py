from django import forms

from utils.filter_widget_fields import filter_widget_fields
from .base import BaseWidgetHandler
from ..models import Widget


class ImageWidgetHandler(BaseWidgetHandler):
    def __init__(self):
        self.widget_type = 'image'

    class ImageWidgetAdminForm(forms.ModelForm):
        image_url = forms.CharField(required=False, label="Image URL", widget=forms.TextInput(attrs={'class': 'vTextField'}))

        class Meta:
            model = Widget
            fields = ('type',)

    def get_form(self, request, obj=None, **kwargs):
        form = self.ImageWidgetAdminForm

        if obj and obj.config:
            image_config = obj.config.get('image', {})
            form.base_fields['image_url'].initial = image_config.get('image_url', '')

        return form

    @filter_widget_fields(['image_url'])
    def save_model(self, request, obj, form, change):
        image_url = form.cleaned_data.get('image_url')

        if obj.config is None:
            obj.config = {}
        if 'image' not in obj.config:
            obj.config['image'] = {}

        obj.config['image']['image_url'] = image_url

        obj.save()
