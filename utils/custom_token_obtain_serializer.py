from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.consultant.models import Consultant
from user.customer.models import Customer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        refresh = self.get_token(user)
        access = refresh.access_token

        data['refresh'] = str(refresh)
        data['access'] = str(access)

        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        if Customer.objects.filter(email=user.email).exists():
            token['user_type'] = 'customer'
        elif Consultant.objects.filter(email=user.email).exists():
            token['user_type'] = 'consultant'

        return token
