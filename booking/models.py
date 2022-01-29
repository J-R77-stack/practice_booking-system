from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

class Booking(models.Model):
    
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=80, null=True)
    appointment_date_and_time = models.DateTimeField(null=True)

    def validate_date(reservation_date_and_time):
        
        if reservation_date_and_time < timezone.now():
            raise ValidationError("Sorry no available appointments. Please try another day or time")
    appointment_date_and_time = models.DateTimeField(null=True,blank=True,validators=[validate_date])
    
    phone_number = models.CharField(null=True, blank=True, max_length=16)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        
        unique_together = ('user', 'name',
                           'appointment_date_and_time')
        ordering = ["created_on"]

    def __str__(self):
        """
        Function to return object model
        items as string.
        """
        return f' User {self.user} has made an appointment \
                   for {self.name}\
                   for {self.appointment_date_and_time}.'



