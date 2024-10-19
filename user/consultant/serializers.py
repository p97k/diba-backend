from rest_framework import serializers
from .models import Consultant

class ConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultant
        fields = ['id', 'email', 'first_name', 'last_name', 'national_id', 'phone_number', 'gender', 'service', 'is_active']
