from rest_framework.views import APIView
from rest_framework import permissions, status
from reservation.reservation_system.permissions import IsCustomer
from user.consultant.models import Consultant
from user.consultant.serializers import ConsultantSerializer
from utils.response import CustomResponse

class ConsultantListByServiceTypeView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsCustomer]

    def get(self, request):
        service_type = request.query_params.get('service_type')

        if service_type and service_type not in dict(Consultant.SERVICE_TYPES):
            return CustomResponse.custom(status.HTTP_400_BAD_REQUEST, "Invalid service type.")

        consultants = Consultant.objects.all()
        if service_type:
            consultants = consultants.filter(service=service_type)

        if not consultants.exists():
            return CustomResponse.not_found()

        serializer = ConsultantSerializer(consultants, many=True)
        return CustomResponse.resolve(serializer.data)
