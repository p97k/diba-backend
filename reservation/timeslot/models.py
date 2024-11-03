from django.db import models
from user.consultant.models import Consultant

class TimeSlot(models.Model):
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.consultant} | {self.start_time} to {self.end_time}"
