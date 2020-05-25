from django.shortcuts import render, HttpResponse
from .models import Appointment
from hms.models import Person
from django.contrib.auth.models import User, Group
from patient.models import Patient
from doctor.models import Doctor

def p_appointment(request):
    person = Person(user=User.objects.get(username=request.user))
    print(request.user, person.type, person.user.username)
    patient = Patient.objects.get(person=person)
    appointments = Appointment.objects.filter(patient=patient).order_by('date')
    print(appointments)
    return render(request, 'patient/appointments.html', { 'appointments': appointments, 'person' : person})

def d_appointment(request):
    person = Person(user=User.objects.get(username=request.user))
    print(request.user, person.type, person.user.username)
    doctor = Doctor.objects.get(person=person)
    appointments = Appointment.objects.filter(doctor=doctor).order_by('date')
    return render(request, 'doctor/appointments.html', {
        'appointments' : appointments, 
        'person' : person
    })


def appointment(request):
    person = Person(user=User.objects.get(username=request.user))
    print(request.user, person.type, person.user.username)
    appointments = Appointment.objects.all().order_by('date')
    return render(request, 'receptionist/appointments.html', { 'appointments': appointments, 'person': person})

