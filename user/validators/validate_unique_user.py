from django.core.exceptions import ValidationError
from django.apps import apps

def validate_unique_email_and_username(email, username):
    Customer = apps.get_model('user', 'Customer')
    Consultant = apps.get_model('user', 'Consultant')

    if Customer.objects.filter(email=email).exists() or Consultant.objects.filter(email=email).exists():
        raise ValidationError("A user with this email already exists.")

    if Customer.objects.filter(first_name=username).exists() or Consultant.objects.filter(first_name=username).exists():
        raise ValidationError("A user with this username already exists.")
