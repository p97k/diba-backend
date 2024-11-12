from rest_framework import generics
from user.consultant.models import Consultant
from user.consultant.serializers import ConsultantSerializer
from utils.response import CustomResponse

class ConsultantDetailView(generics.RetrieveAPIView):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        consultant_data = response.data

        result = {
            "id": consultant_data['id'],
            "first_name": consultant_data['first_name'],
            "last_name": consultant_data['last_name'],
            "phone_number": consultant_data['phone_number'],
            "gender": consultant_data['gender'],
            "service": consultant_data['service'],
        }

        return CustomResponse.resolve(result)