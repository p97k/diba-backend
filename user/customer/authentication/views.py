from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from utils.response import CustomResponse
from .serializers import CustomerLoginSerializer

class CustomerLoginView(APIView):
    def post(self, request):
        serializer = CustomerLoginSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.validated_data

            refresh = RefreshToken.for_user(customer)
            access_token = refresh.access_token

            result = {
                'refresh_token': str(refresh),
                'access_token': str(access_token),
                'message': "Login successful"
            }

            return CustomResponse.resolve(result)

        return CustomResponse.reject()
