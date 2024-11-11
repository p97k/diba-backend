from django.contrib.auth.backends import ModelBackend

from user.consultant.models import Consultant
from user.customer.models import Customer


class CustomModelBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        if kwargs.get('username') is None or kwargs.get('password') is None:
            return None

        try:
            user = Consultant.objects.get(username=kwargs['username'])
        except Consultant.DoesNotExist:
            try:
                user = Customer.objects.get(username=kwargs['username'])
            except Customer.DoesNotExist:
                return None

        if user.check_password(kwargs['password']) and self.user_can_authenticate(user):
            return user
        return None