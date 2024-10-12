from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from dynamic_pages.page.serializers import PageSerializer
from dynamic_pages.page.models import Page
from dynamic_pages.widget.widget_views.widget_view_factory import WidgetViewFactory
from utils.response import CustomResponse
from django.shortcuts import render

class DynamicPageView(APIView):
    def get(self, request, route):
        page = get_object_or_404(Page, route=route)
        serializer = PageSerializer(page)
        serializedData = serializer.data

        preparedWidgets = []
        for widget in serializedData['widgets']:
            widgetView = WidgetViewFactory.get_view(widget['type'])
            preparedData = widgetView.handle_widget_data(widget)
            preparedWidgets.append(preparedData)

        result = {
            'id': serializedData['id'],
            'title' : serializedData['title'],
            'page_name' : serializedData['route'],
            'widgets' : preparedWidgets,
        }

        return CustomResponse.resolve(result)

def load_post_widget_fields(request):
    return render(request, 'admin/dynamic_pages/widget/types/post_widget.html')

def load_image_widget_fields(request):
    return render(request, 'admin/dynamic_pages/widget/types/image_widget.html')