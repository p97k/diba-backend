from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from dynamic_pages.page.serializers import PageSerializer
from dynamic_pages.page.models import Page
from utils.response import CustomResponse


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
