from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from reservation.reservation_system.models import Reservation
from reservation.reservation_system.permissions import IsCustomer
from reservation.serializers.reserve_time_slot_serializer import ReserveTimeSlotSerializer
from reservation.timeslot.models import TimeSlot
from user.customer.models import Customer
from utils.response import CustomResponse

class ReserveTimeSlotView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsCustomer]

    def post(self, request):
        serializer = ReserveTimeSlotSerializer(data=request.data)

        if serializer.is_valid():
            time_slot_id = serializer.validated_data['time_slot_id']
            consultant_id = serializer.validated_data['consultant_id']

            try:
                time_slot = TimeSlot.objects.get(id=time_slot_id, consultant__id=consultant_id)

                if time_slot.reservation:
                    return CustomResponse.custom(status.HTTP_400_BAD_REQUEST, "Time slot already reserved.")

                customer = Customer.objects.get(user=request.user)

                reservation = Reservation.objects.create(
                    customer=customer,
                    time_slot=time_slot
                )

                return CustomResponse.resolve({
                    "message": "Reservation successful.",
                    "reservation_id": reservation.id,
                    "time_slot": {
                        "date": time_slot.date,
                        "start_time": time_slot.start_time,
                        "end_time": time_slot.end_time
                    }
                })

            except TimeSlot.DoesNotExist:
                return CustomResponse.not_found()

            except Exception as e:
                return CustomResponse.custom(status.HTTP_400_BAD_REQUEST, str(e))

        else:
            return CustomResponse.custom(status.HTTP_400_BAD_REQUEST, "Bad Request", serializer.errors)
