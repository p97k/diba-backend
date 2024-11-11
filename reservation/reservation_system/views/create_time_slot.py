from rest_framework import permissions
from rest_framework.views import APIView
from reservation.reservation_system.permissions import IsConsultant
from reservation.serializers.time_slot_create_serializer import TimeSlotCreateSerializer
from rest_framework import status
from user.consultant.models import Consultant
from utils.response import CustomResponse

class CreateTimeSlotView(APIView):
    # permission_classes = [permissions.IsAuthenticated, IsConsultant]

    def post(self, request):
        try:
            consultant = Consultant.objects.get(email=request.user.email)
        except Consultant.DoesNotExist:
            return CustomResponse.not_found()

        serializer = TimeSlotCreateSerializer(data=request.data, context={'consultant': consultant})
        if serializer.is_valid():
            time_slot = serializer.save()
            return CustomResponse.resolve(TimeSlotCreateSerializer(time_slot).data)
        return CustomResponse.custom(status.HTTP_400_BAD_REQUEST, 'Bad Request', serializer.errors)
