from rest_framework import serializers
from datetime import datetime, timedelta
from reservation.timeslot.models import TimeSlot

class TimeSlotCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ['consultant', 'start_time', 'end_time', 'is_available']

    def validate(self, data):
        """
        Validate the time slot data
        """
        consultant = self.context['consultant']

        current_datetime = datetime.now()
        selected_datetime = datetime.combine(data['date'], data['start_time'])

        if selected_datetime <= current_datetime:
            raise serializers.ValidationError("Time slot must be in the future.")

        start_time = data['start_time']
        end_time = data['end_time']

        if start_time >= end_time:
            raise serializers.ValidationError("Start time must be earlier than end time.")

        existing_slots = TimeSlot.objects.filter(
            consultant=consultant,
            date=data['date']
        ).filter(
            start_time__lt=end_time,
            end_time__gt=start_time
        )

        if existing_slots.exists():
            raise serializers.ValidationError("Time slot overlaps with an existing slot.")

        work_start = datetime.combine(data['date'], datetime.min.time()) + timedelta(hours=9)
        work_end = datetime.combine(data['date'], datetime.min.time()) + timedelta(hours=18)

        if selected_datetime < work_start or selected_datetime > work_end:
            raise serializers.ValidationError("Time slot must be within working hours (9 AM to 6 PM).")

        return data

    def create(self, validated_data):
        """
        Create the time slot with the associated consultant.
        """
        consultant = self.context['consultant']
        time_slot = TimeSlot.objects.create(
            consultant=consultant,
            **validated_data
        )
        return time_slot
