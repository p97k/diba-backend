from django.db import models

from reservation.timeslot.models import TimeSlot
from user.customer.models import Customer


class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reservations')
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, related_name='reservations')
    date = models.DateField()

    class Meta:
        unique_together = ('time_slot', 'date')

    def __str__(self):
        return f"{self.customer} reserved {self.time_slot} on {self.date}"
