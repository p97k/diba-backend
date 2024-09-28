from rest_framework.views import APIView
from utils.response import CustomResponse
from .serializers import CustomerSignUpSerializer

class CustomerSignUpView(APIView):
    def post(self, request):
        serializer = CustomerSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse.resolve()
        return CustomResponse.reject()
