from rest_framework.views import APIView

from utils.response import CustomResponse


class ConsultantListView(APIView):
    def get(self, request):
        return CustomResponse.reject()

class ConsultantDetailView(APIView):
    def get(self, request, id):
        return CustomResponse.reject()
