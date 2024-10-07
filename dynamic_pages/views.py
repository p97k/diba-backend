from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from dynamic_pages.page.serializers import PageSerializer
from dynamic_pages.page.models import Page
from utils.response import CustomResponse
from django.shortcuts import render

class DynamicPageView(APIView):
    def get(self, request, route):
        page = get_object_or_404(Page, route=route)
        serializer = PageSerializer(page)
        serializedData = serializer.data

        result = {
            'id': serializedData['id'],
            'title' : serializedData['title'],
            'page_name' : serializedData['route'],
            'widgets' : serializedData['widgets'],
        }

        return CustomResponse.resolve(result)

def load_post_widget_fields(request):
    return render(request, 'admin/dynamic_pages/widget/types/post_widget.html')

def load_image_widget_fields(request):
    return render(request, 'admin/dynamic_pages/widget/types/image_widget.html')