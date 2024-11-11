from rest_framework import status
from rest_framework.views import APIView
from utils.custom_token_obtain_serializer import CustomTokenObtainPairSerializer
from utils.response import CustomResponse
from .serializers import CustomerLoginSerializer

class CustomerLoginView(APIView):
    def post(self, request):
        login_serializer = CustomerLoginSerializer(data=request.data)
        if login_serializer.is_valid():
            consultant = login_serializer.validated_data
            token_data = {
                'user_id': consultant.id,
                'email': consultant.email,
                'username': consultant.username,
                'password': request.data['password'],
                'user_type': 'customer',
            }

            token_serializer = CustomTokenObtainPairSerializer(data=token_data)
            if token_serializer.is_valid():
                result = {
                    'refresh_token': token_serializer.validated_data['refresh'],
                    'access_token': token_serializer.validated_data['access'],
                    'user_type': token_serializer.validated_data['user_type'],
                    'message': "Login successful"
                }
                return CustomResponse.resolve(result)

            return CustomResponse.custom(status.HTTP_400_BAD_REQUEST, token_serializer.errors)

        return CustomResponse.custom(status.HTTP_400_BAD_REQUEST, login_serializer.errors)
