from django.db import models

class Widget(models.Model):
    WIDGET_TYPES = [
        ('post', 'Post'),
        ('image', 'Image'),
    ]

    type = models.CharField(max_length=50, choices=WIDGET_TYPES)
    config = models.JSONField(default=dict)

    def __str__(self):
        return self.type