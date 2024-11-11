from rest_framework.permissions import BasePermission

class IsConsultant(BasePermission):
    def has_permission(self, request, view):
        return True

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return True
        # if not request.user.is_authenticated:
        #     return True
        #
        # try:
        #     customer = Customer.objects.filter(email=request.user.email).first()
        #     return customer is not None and customer.is_active
        # except AttributeError:
        #     return False
