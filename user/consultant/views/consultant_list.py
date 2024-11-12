from rest_framework import generics
from user.consultant.models import Consultant
from user.consultant.serializers import ConsultantSerializer
from utils.response import CustomResponse

class ConsultantListView(generics.ListAPIView):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        result = []
        for consultant in response.data:
            result.append(
                {
                    "id": consultant["id"],
                    "first_name": consultant['first_name'],
                    "last_name": consultant['last_name'],
                    "phone_number": consultant['phone_number'],
                    "gender": consultant['gender'],
                    "service": consultant['service'],
                }
            )

        return CustomResponse.resolve(result)