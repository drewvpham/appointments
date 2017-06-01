from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import bcrypt
import re


# Create your models here.
class AppointmentManager(models.Manager):
    def validCheck(self, form_data):
        result = {"valid": True}
        errors = []
        if len(form_data['name'])<2:
            errors.append("Name must be at least 2 characters long.")
            result["valid"]=False
        if Appointment.objects.filter(day = form_data['day']).first() and Appointment.objects.filter(time = form_data['time']).first():
            result["valid"]=False
            errors.append("That appointment has already been taken. Please select a different time")
        result['errors'] = errors
        return result

class Appointment(models.Model):
    name = models.CharField(max_length=255)
    day=models.DateField()
    time=models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


    objects = AppointmentManager()
