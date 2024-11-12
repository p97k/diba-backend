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
        return CustomResponse.resolve(consultant_data)