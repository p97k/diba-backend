from rest_framework import serializers
from ..models import Consultant
from django.contrib.auth.hashers import check_password
import re

class ConsultantLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        error_messages={'min_length': 'Password must be at least 8 characters long'}
    )

    def validate_email(self, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise serializers.ValidationError("Please enter a valid email address")
        return value

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            consultant = Consultant.objects.get(email=email)
        except Consultant.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")

        if not check_password(password, consultant.password):
            raise serializers.ValidationError("Invalid email or password")

        return consultant
