from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from user.consultant.models import Consultant
from user.customer.models import Customer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        if Customer.objects.filter(email=user.email).exists():
            user_type = 'customer'
        elif Consultant.objects.filter(email=user.email).exists():
            user_type = 'consultant'
        else:
            raise serializers.ValidationError("User type could not be determined.")

        data['user_type'] = user_type

        return data
