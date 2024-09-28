from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND


class CustomResponse:
    @staticmethod
    def custom(status, message, data=None):
        if data is None:
            data = {}
        return Response({
            'status': status,
            'message': message,
            'data': data
        })

    @classmethod
    def resolve(cls, data=None):
        if data is None:
            data = {}
        return cls.custom(HTTP_200_OK, "OK", data)

    @classmethod
    def reject(cls):
        return cls.custom(HTTP_400_BAD_REQUEST, "Bad Request")

    @classmethod
    def not_found(cls):
        return cls.custom(HTTP_404_NOT_FOUND, "Not Found")