from rest_framework.views import APIView
from rest_framework import status, permissions
from reservation.serializers.time_slot_create_serializer import TimeSlotCreateSerializer
from user.consultant.models import Consultant
from utils.response import CustomResponse
from reservation.reservation_system.permissions import IsConsultant

class CreateTimeSlotView(APIView):
    # permission_classes = [permissions.IsAuthenticated, IsConsultant]

    def post(self, request):
        consultant = Consultant.objects.get(email=request.user)

        serializer = TimeSlotCreateSerializer(data=request.data, context={'consultant': consultant})

        if serializer.is_valid():
            time_slot = serializer.save()

            return CustomResponse.resolve({
                "message": "Time slot created successfully.",
                "time_slot": {
                    "id": time_slot.id,
                    "start_time": time_slot.start_time,
                    "end_time": time_slot.end_time,
                    "is_available": time_slot.is_available
                }
            })

        return CustomResponse.custom(status.HTTP_400_BAD_REQUEST, serializer.errors)
