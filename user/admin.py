from .customer.models import Customer
from django.contrib import admin

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'national_id', 'phone_number', 'is_active')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number', 'national_id')
