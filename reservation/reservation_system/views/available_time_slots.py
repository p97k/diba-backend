from rest_framework.views import APIView
from rest_framework import permissions
from django.utils import timezone
from reservation.reservation_system.permissions import IsCustomer
from reservation.timeslot.models import TimeSlot
from user.consultant.models import Consultant
from reservation.serializers.time_slot_serializer import TimeSlotSerializer
from utils.response import CustomResponse

class AvailableTimeSlotsView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsCustomer]

    def get(self, request, consultant_id):
        try:
            consultant = Consultant.objects.get(id=consultant_id)
        except Consultant.DoesNotExist:
            return CustomResponse.not_found()

        current_date = timezone.now().date()
        available_time_slots = TimeSlot.objects.filter(
            consultant=consultant,
            date__gte=current_date
        ).exclude(reservations__isnull=False).order_by('date', 'start_time')

        serializer = TimeSlotSerializer(available_time_slots, many=True)
        return CustomResponse.resolve(serializer.data)
