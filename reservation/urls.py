from django.urls import path
from reservation.reservation_system.views.available_time_slots import AvailableTimeSlotsView
from reservation.reservation_system.views.consultant_list_by_service_type import ConsultantListByServiceTypeView
from reservation.reservation_system.views.create_time_slot import CreateTimeSlotView
from reservation.reservation_system.views.reservation import ReserveTimeSlotView

urlpatterns = [
    path('v1/create-time-slot/', CreateTimeSlotView.as_view(), name='create-time-slot'),
    path('v1/consultants-by-service/', ConsultantListByServiceTypeView.as_view(), name='consultant-list-by-service-type'),
    path('v1/<int:consultant_id>/available-time-slots/', AvailableTimeSlotsView.as_view(),
         name='available-time-slots'),
    path('v1/reserve/', ReserveTimeSlotView.as_view(), name='reserve-time-slot'),
]
