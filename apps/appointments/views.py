from django.shortcuts import render, redirect
from models import *
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render(request, 'appointments/index.html')


def add_appointment(request):
    if request.method=='POST':
        check=Appointment.objects.validCheck(request.POST)
        if check['valid']==True:
            appointment=Appointment.objects.create(name=request.POST['name'], day=request.POST['day'], time=request.POST['time'])
            request.session['day']=appointment.day
            request.session['time']=appointment.time
            return redirect('/success')
            

        for error in check['errors']:
            messages.error(request, error)
    return redirect('/')


def success(request):

    return render(request, 'appointments/success.html')
