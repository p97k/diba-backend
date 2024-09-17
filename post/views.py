from rest_framework.response import Response
from rest_framework.views import APIView


class PostApiView(APIView):
    def get(self, request):
        return Response('post get view')