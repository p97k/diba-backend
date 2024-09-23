from rest_framework import serializers
from ..models import Customer

class CustomerSignUpSerializer(serializers.ModelSerializer):
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

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        customer = Customer(
            email=validated_data['email'],
            name=validated_data['first_name'],
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
