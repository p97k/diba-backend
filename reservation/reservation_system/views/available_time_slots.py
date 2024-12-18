from rest_framework.views import APIView
from reservation.timeslot.models import TimeSlot
from user.consultant.models import Consultant
from reservation.serializers.time_slot_serializer import TimeSlotSerializer
from utils.response import CustomResponse

class AvailableTimeSlotsView(APIView):
    def get(self, request, consultant_id):
        try:
            consultant = Consultant.objects.get(id=consultant_id)
        except Consultant.DoesNotExist:
            return CustomResponse.not_found()

        available_time_slots = TimeSlot.objects.filter(
            consultant=consultant,
        ).exclude(reservations__isnull=False).order_by('start_time')

        serializer = TimeSlotSerializer(available_time_slots, many=True)
        return CustomResponse.resolve(serializer.data)
