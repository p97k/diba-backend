from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Customer(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10, blank=False)
    address = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    gender = models.IntegerField(default=0)
    marital_status = models.IntegerField(default=0)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.email