from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from utils.response import CustomResponse
from .serializers import ConsultantLoginSerializer

class ConsultantLoginView(APIView):
    def post(self, request):
        print(request.data)
        serializer = ConsultantLoginSerializer(data=request.data)
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

        return CustomResponse.custom(status.HTTP_400_BAD_REQUEST, serializer.errors)
