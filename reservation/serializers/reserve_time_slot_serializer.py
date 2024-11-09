from rest_framework import serializers
from reservation.timeslot.models import TimeSlot
from user.consultant.models import Consultant

class ReserveTimeSlotSerializer(serializers.Serializer):
    time_slot_id = serializers.IntegerField()
    consultant_id = serializers.IntegerField()

    def validate_time_slot_id(self, value):
        """
        Validate that the time slot exists and is available.
        """
        try:
            time_slot = TimeSlot.objects.get(id=value)
            if time_slot.reservation:
                raise serializers.ValidationError("This time slot has already been reserved.")
        except TimeSlot.DoesNotExist:
            raise serializers.ValidationError("The selected time slot does not exist.")
        return value

    def validate_consultant_id(self, value):
        """
        Validate that the consultant exists.
        """
        if not Consultant.objects.filter(id=value).exists():
            raise serializers.ValidationError("The selected consultant does not exist.")
        return value
