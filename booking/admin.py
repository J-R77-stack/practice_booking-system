from django.contrib import admin
from .models import Booking
from django.contrib.admin import ModelAdmin

@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    """
    Class registered to represent model in admin database.
    """
    list_display = ('user', 'name',
                    'phone_number',
                    'email',
                    'appointment_date_and_time')
    search_fields = ('name',
                     'phone_number',
                     'email',
                     'appointment_date_and_time')
    list_filter = ('name',
                   'phone_number',
                   'email', 
                   'appointment_date_and_time')
    actions = ['approve_booking']

    

