from rest_framework import serializers
from reservation.timeslot.models import TimeSlot
from django.utils import timezone

class TimeSlotCreateSerializer(serializers.Serializer):
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()

    def validate(self, attrs):
        """
        Validate that:
        - start time is before the end time
        - start time is not in the past
        - no other time slot exists for the same consultant with overlapping times
        """
        start_time = attrs.get("start_time")
        end_time = attrs.get("end_time")
        consultant = self.context.get("consultant")

        if start_time < timezone.now():
            raise serializers.ValidationError("Start time cannot be in the past.")

        if start_time >= end_time:
            raise serializers.ValidationError("Start time must be before end time.")

        overlapping_slots = TimeSlot.objects.filter(
            consultant=consultant,
            is_available=True,
            start_time__lt=end_time,
            end_time__gt=start_time
        )

        if overlapping_slots.exists():
            raise serializers.ValidationError("This time slot overlaps with an existing time slot for this consultant.")

        exact_match = TimeSlot.objects.filter(
            consultant=consultant,
            start_time=start_time,
            end_time=end_time
        ).exists()

        if exact_match:
            raise serializers.ValidationError("A time slot with the same start and end time already exists for this consultant.")

        return attrs

    def create(self, validated_data):
        """
        Create a new time slot for the consultant.
        """
        consultant = self.context.get("consultant")
        start_time = validated_data.get("start_time")
        end_time = validated_data.get("end_time")

        time_slot = TimeSlot.objects.create(
            consultant=consultant,
            start_time=start_time,
            end_time=end_time,
            is_available=True
        )
        return time_slot
