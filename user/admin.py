from django.contrib import admin
from .customer.models import Customer
from django.contrib import admin

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'last_name', 'is_active')
    search_fields = ('email', 'name', 'last_name')
