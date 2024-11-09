from rest_framework import serializers
from reservation.timeslot.models import TimeSlot

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ['id', 'start_time', 'end_time', 'consultant', 'is_available']
