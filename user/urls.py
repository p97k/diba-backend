from django.urls import path
from user.consultant.authentication.views import ConsultantLoginView
from user.consultant.views.consultant_detail import ConsultantDetailView
from user.consultant.views.consultant_list import ConsultantListView
from user.consultant.views.consultant_list_by_service_type import ConsultantListByServiceTypeView
from user.customer.authentication.views import CustomerLoginView
from user.customer.registration.views import CustomerSignUpView

urlpatterns = [
    path('v1/customer/register/', CustomerSignUpView.as_view(), name='customer_signup'),
    path('v1/customer/auth/', CustomerLoginView.as_view(), name='customer_login'),
    path('v1/consultant/auth/', ConsultantLoginView.as_view(), name='consultant_login'),
    path('v1/consultant/list/', ConsultantListView.as_view(), name='consultant_list'),
    path('v1/consultant/service-base-list/', ConsultantListByServiceTypeView.as_view(), name='consultant-list-by-service-type'),
    path('v1/consultant/detail/<str:id>/', ConsultantDetailView.as_view(), name='consultant_detail'),
]