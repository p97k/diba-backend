from django.db import models
from dynamic_pages.widget.models import Widget


class Page(models.Model):
    title = models.CharField(max_length=255)
    route = models.CharField(max_length=255, unique=True)
    widgets = models.ManyToManyField(Widget, related_name='pages')

    def __str__(self):
        return self.title
