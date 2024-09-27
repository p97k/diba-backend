from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ..models import Customer
import re

class CustomerSignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
        UniqueValidator(queryset=Customer.objects.all(), message="Email already exists")
    ])

    postal_code = serializers.CharField(required=True, min_length=10, max_length=10, error_messages={
        'min_length': 'Postal code must be exactly 10 digits',
        'max_length': 'Postal code must be exactly 10 digits'
    })

    password = serializers.CharField(write_only=True, min_length=8, error_messages={
        'min_length': 'Password must be at least 8 characters long'
    })

    phone_number = serializers.CharField(
        required=True,
        min_length=11,
        max_length=11,
        error_messages={
            'min_length': 'Phone number must be exactly 11 digits',
            'max_length': 'Phone number must be exactly 11 digits'
        }
    )

    class Meta:
        model = Customer
        fields = [
            'email',
            'first_name',
            'last_name',
            'national_id',
            'phone_number',
            'postal_code',
            'address',
            'age',
            'gender',
            'marital_status',
            'password'
        ]

    def validate_email(self, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise serializers.ValidationError("Please enter a valid email address")
        return value

    def validate_postal_code(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Postal code must contain only digits")
        return value

    def validate_phone_number(self, value):
        if not re.match(r"^09\d{9}$", value):
            raise serializers.ValidationError("Phone number must be exactly 11 digits and start with '09'")
        return value

    def create(self, validated_data):
        customer = Customer(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            national_id=validated_data['national_id'],
            phone_number=validated_data['phone_number'],
            postal_code=validated_data['postal_code'],
            address=validated_data['address'],
            age=validated_data['age'],
            gender=validated_data['gender'],
            marital_status=validated_data['marital_status'],
        )
        customer.set_password(validated_data['password'])
        customer.save()
        return customer
