from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone

class Customer(models.Model):
    email = models.EmailField(unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=255, blank=False, default="")
    postal_code = models.CharField(max_length=10, blank=False)
    address = models.CharField(max_length=255, blank=False)
    age = models.IntegerField(default=0)
    gender = models.IntegerField(default=0)
    marital_status = models.IntegerField(default=0)
    password = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.email