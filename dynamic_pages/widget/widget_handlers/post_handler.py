from django import forms

from utils.filter_widget_fields import filter_widget_fields
from .base import BaseWidgetHandler
from ..models import Widget


class PostWidgetHandler(BaseWidgetHandler):
    def __init__(self):
        self.widget_type = 'post'

    class PostWidgetAdminForm(forms.ModelForm):
        DIRECTION_CHOICES = [
            ('LTR', 'Left to Right'),
            ('RTL', 'Right to Left'),
        ]

        title = forms.CharField(required=False, label="Title", widget=forms.TextInput(attrs={'class': 'vTextField'}))
        image_url = forms.CharField(required=False, label="Image URL", widget=forms.TextInput(attrs={'class': 'vTextField'}))
        description = forms.CharField(required=False, label="Description", widget=forms.Textarea(attrs={'class': 'vLargeTextField'}))
        direction = forms.ChoiceField(choices=DIRECTION_CHOICES, required=False, label="Direction", widget=forms.Select(attrs={'class': 'vSelectField'}))

        class Meta:
            model = Widget
            fields = ('type',)

    def get_form(self, request, obj=None, **kwargs):
        form = self.PostWidgetAdminForm

        if obj and obj.config:
            post_config = obj.config.get('post', {})
            form.base_fields['title'].initial = post_config.get('title', '')
            form.base_fields['image_url'].initial = post_config.get('image_url', '')
            form.base_fields['description'].initial = post_config.get('description', '')
            form.base_fields['direction'].initial = post_config.get('direction', '')

        return form

    @filter_widget_fields(['title', 'description', 'image_url', 'direction'])
    def save_model(self, request, obj, form, change):
        title = form.cleaned_data.get('title')
        image_url = form.cleaned_data.get('image_url')
        description = form.cleaned_data.get('description')
        direction = form.cleaned_data.get('direction')

        if obj.config is None:
            obj.config = {}
        if 'post' not in obj.config:
            obj.config['post'] = {}

        obj.config['post']['title'] = title
        obj.config['post']['image_url'] = image_url
        obj.config['post']['description'] = description
        obj.config['post']['direction'] = direction

        obj.save()
