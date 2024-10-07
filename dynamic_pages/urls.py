from django.urls import path
from .views import DynamicPageView
from . import views

urlpatterns = [
    path('<str:route>/', DynamicPageView.as_view(), name='dynamic-page'),

    path('admin/widgets/load-post-fields/', views.load_post_widget_fields, name='load_post_widget_fields'),
    path('admin/widgets/load-image-fields/', views.load_image_widget_fields, name='load_image_widget_fields'),
]
