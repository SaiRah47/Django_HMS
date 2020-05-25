from django.shortcuts import render, HttpResponse, redirect
from .models import Appointment
from hms.models import Person, Receptionist
from django.contrib.auth.models import User, Group
from patient.models import Patient
from doctor.models import Doctor 
from datetime import datetime

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
    if request.method == 'POST':
        patient = request.POST['patient']
        doctor = request.POST['doctor']
        date_time = request.POST['date'] +  'T' + request.POST['time']
        status = request.POST['status']
        print(date_time)
        date_time = datetime(*[int(v) for v in date_time.replace('T', '-').replace(':', '-').split('-')])
        patient_p = Person.objects.get(user=User.objects.get(username=patient))
        doctor_p  = Person.objects.get(user=User.objects.get(username=doctor))
        receptionist_p  = Person.objects.get(user=User.objects.get(username=request.user))
        appoint = Appointment(patient=Patient.objects.get(person=patient_p), doctor=Doctor.objects.get(person=doctor_p), receptionist=Receptionist.objects.get(person=receptionist_p))
        appoint.date = date_time
        appoint.status = status

        appoint.save()
        return redirect('appointment')


    person = Person(user=User.objects.get(username=request.user))
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    print(request.user, person.type, person.user.username)
    appointments = Appointment.objects.all().order_by('date')
    return render(request, 'receptionist/appointments.html', { 'appointments': appointments, 'person': person, 'patients': patients, 'doctors': doctors})


def change_appointment(request, appointment_id):
    person = Person(user=User.objects.get(username=request.user))
    appointment = Appointment.objects.get(pk=appointment_id)
    doctors = Doctor.objects.all()
    return render(request, 'receptionist/change.html', {
        'person': person, 'appointment': appointment, 'doctors': doctors
    })

def updateAppointment(request):
    if request.method == 'POST':
        id = request.POST['id']
        doctor = request.POST['doctor']
        date_time = request.POST['date'] +  'T' + request.POST['time']
        status = request.POST['status']
        date_time = datetime(*[int(v) for v in date_time.replace('T', '-').replace(':', '-').split('-')])
        appoint = Appointment.objects.get(pk=int(id))
        person  = Person.objects.get(user=User.objects.get(username=doctor))
        doctor_p = Doctor.objects.get(person=person)
        person_rec =  Person.objects.get(user=User.objects.get(username=request.user))
        receptionist_p = Receptionist.objects.get(person=person_rec)
        appoint.doctor = doctor_p
        appoint.date = date_time
        appoint.status = status
        appoint.receptionist = receptionist_p
        appoint.save()
        return redirect('appointment')


def delete_appointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    appointment.delete()
    return redirect('appointment')
