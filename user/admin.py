from .consultant.models import Consultant
from .customer.models import Customer
from django.contrib import admin

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'national_id', 'phone_number', 'is_active')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number', 'national_id')

    def save_model(self, request, obj, form, change):
        password = form.cleaned_data.get("password")
        if password:
            obj.set_password(password)
        super().save_model(request, obj, form, change)

@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'service', 'is_active')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number', 'service', 'national_id')

    def save_model(self, request, obj, form, change):
        password = form.cleaned_data.get("password")
        if password:
            obj.set_password(password)
        super().save_model(request, obj, form, change)
