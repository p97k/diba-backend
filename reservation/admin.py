from django.contrib import admin

from reservation.reservation_system.models import Reservation
from reservation.timeslot.models import TimeSlot


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'consultant', 'start_time', 'end_time', 'is_available')
    search_fields = ('consultant__email', 'start_time', 'end_time', 'is_available')

@admin.register(Reservation)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'customer_id', 'time_slot')
    search_fields = ('id', 'customer__email', 'time_slot__consultant__email')
