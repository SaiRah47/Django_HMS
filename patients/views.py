from django.shortcuts import render, redirect
from hms.models import Person, Receptionist
from patient.models import Patient
from django.contrib.auth.models import User
from .models import Recep_patient

def patients(request):
    user = User.objects.get(username=request.user)
    receptionist = Receptionist.objects.get(
        person=Person.objects.get(user=user))
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        gender = request.POST["gender"]
        age = request.POST["age"]
        obj = Recep_patient(receptionist=receptionist, name=name,
                       phone=phone, email=email, gender=gender, age=age)
        obj.save()

    patients = Recep_patient.objects.filter(receptionist=receptionist)
    return render(request, 'receptionist/patients.html', {'patients': patients})


def delete_patient(request, patient_id=None):
    user = User.objects.get(username=request.user)
    receptionist = Receptionist.objects.get(
        person=Person.objects.get(user=user))
    patient = Recep_patient.objects.get(id=patient_id)
    patient.delete()
    patients = Recep_patient.objects.filter(receptionist=receptionist)
    return redirect('rpatients')


def update_patient(request, patient_id=None):
    patient = Recep_patient.objects.get(id=patient_id)
    print(patient)
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        gender = request.POST["gender"]
        age = request.POST["age"]
        patient.name = name
        patient.phone = phone
        patient.email = email
        patient.gender = gender
        patient.age = age
        patient.save()
        return redirect('rpatients')
    return render(request, 'receptionist/update_patient.html', {'patients': patient})
