from rest_framework import authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from user.consultant.models import Consultant
from user.customer.models import Customer


class CustomUserJWTAuthentication(JWTAuthentication, authentication.BaseAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)

        user_id = validated_token.get("user_id")
        user_type = validated_token.get("user_type")

        if user_type == 'customer':
            user = Customer.objects.filter(id=user_id).first()
        elif user_type == 'consultant':
            user = Consultant.objects.filter(id=user_id).first()
        else:
            raise AuthenticationFailed("Invalid user type")

        if not user:
            raise AuthenticationFailed("User not found")

        return user, validated_token
