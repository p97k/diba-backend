from rest_framework import status
from rest_framework.views import APIView
from utils.response import CustomResponse
from .serializers import CustomerSignUpSerializer

class CustomerSignUpView(APIView):
    def post(self, request):
        serializer = CustomerSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse.resolve()
        return CustomResponse.custom(status.HTTP_400_BAD_REQUEST, serializer.errors)
