from django.contrib import admin

from reservation.timeslot.models import TimeSlot


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'consultant', 'start_time', 'end_time', 'is_available')
    search_fields = ('consultant__email', 'start_time', 'end_time', 'is_available')
