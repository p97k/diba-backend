from django import forms
from .base import BaseWidgetHandler
from ..models import Widget


class PostWidgetHandler(BaseWidgetHandler):
    class PostWidgetAdminForm(forms.ModelForm):
        title = forms.CharField(required=False, label="Title", widget=forms.TextInput(attrs={'class': 'vTextField'}))
        description = forms.CharField(required=False, label="Description", widget=forms.Textarea(attrs={'class': 'vLargeTextField'}))

        class Meta:
            model = Widget
            fields = ('type',)

    def get_form(self, request, obj=None, **kwargs):
        form = self.PostWidgetAdminForm

        if obj and obj.config:
            post_config = obj.config.get('post', {})
            form.base_fields['title'].initial = post_config.get('title', '')
            form.base_fields['description'].initial = post_config.get('description', '')

        return form

    def save_model(self, request, obj, form, change):
        title = form.cleaned_data.get('title')
        description = form.cleaned_data.get('description')

        if obj.config is None:
            obj.config = {}
        if 'post' not in obj.config:
            obj.config['post'] = {}

        obj.config['post']['title'] = title
        obj.config['post']['description'] = description

        obj.save()
