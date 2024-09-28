from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from dynamic_pages.page.serializers import PageSerializer
from dynamic_pages.page.models import Page

class DynamicPageView(APIView):
    def get(self, request, route):
        page = get_object_or_404(Page, route=route)
        serializer = PageSerializer(page)
        return JsonResponse(serializer.data, status=200)
