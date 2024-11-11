from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from user.validators.validate_unique_user import validate_unique_email_and_username


class Consultant(models.Model):
    SERVICE_TYPES = [
        ('children', 'کودک و نوجوان'),
        ('personal', 'مشاوره فردی'),
        ('obstetrics', 'زنان و زایمان'),
    ]

    GENDER_TYPES = [
        ('man', 'آقا'),
        ('woman', 'خانم'),
    ]

    email = models.EmailField(unique=True, blank=False, null=False)
    username = models.CharField(max_length=255, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    national_id = models.CharField(max_length=10, blank=False)
    phone_number = models.CharField(max_length=255, blank=False)
    gender = models.CharField(max_length=50, choices=GENDER_TYPES)
    service = models.CharField(max_length=50, choices=SERVICE_TYPES)
    password = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def save(self, *args, **kwargs):
        validate_unique_email_and_username(self.email, self.first_name)

        if not self.username:
            self.username = self.email
        super(Consultant, self).save(*args, **kwargs)

    def __str__(self):
        return self.email
