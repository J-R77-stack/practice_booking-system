from django.contrib import admin
from .models import Booking
from django.contrib.admin import ModelAdmin

@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    """
    Class registered to represent model in admin database.
    """
    list_display = ('user', 'name',
                    'appointment_date_and_time',
                    'phone_number',
                    'email')
    search_fields = ('name',
                     'appointment_date_and_time',
                     'phone_number',
                     'email')
    list_filter = ('name',
                   'appointment_date_and_time',
                   'phone_number',
                   'email')
    actions = ['approve_booking']

    

