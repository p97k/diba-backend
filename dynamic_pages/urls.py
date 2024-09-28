from django.urls import path
from .views import DynamicPageView

urlpatterns = [
    path('<str:route>/', DynamicPageView.as_view(), name='dynamic-page'),
]
