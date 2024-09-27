from django.urls import path

from user.customer.registration.views import CustomerSignUpView

urlpatterns = [
    path('customer/register/', CustomerSignUpView.as_view(), name='customer_signup'),
]