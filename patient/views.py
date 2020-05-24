from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from hms.models import Person
from .models import Patient
from doctor.models import Prescription


def profile(request):
    user = request.user
    user = User.objects.get(username=user)
    person = Person.objects.get(user=user)
    users = {
        'firstname': request.user.first_name,
        'lastname': request.user.last_name,
        'email': request.user.email,
    }
    print(users)
    if request.method == 'POST':
        phone = request.POST['phone']
        gender = request.POST['gender']
        address = request.POST['address']
        age = request.POST['age']
        
        if phone and gender and address and age:
            if Patient.objects.filter(person=person).exists():
                patient = Patient.objects.get(person=person)
                patient_val = Patient.objects.filter(person=person).update(person=person, phone=phone, gender=gender, address=address, age=age)
                return render(request, 'patient/profile.html', {'patient': patient, 'users': users, 'person': person})

            obj = Patient.objects.create(person=person, phone=phone, gender=gender, age=age, address=address)
            obj.save()

            return render(request, 'patient/profile.html', {'patient': patient, 'users': users, 'person': person})
        else:
            print("Error Occured: ",phone,gender,address,age)
    patient = Patient.objects.filter(person=person)
    if Patient.objects.filter(person=person).exists():
        patient = Patient.objects.filter(person=person)[0]
        return render(request, 'patient/profile.html', {'patient': patient, 'users': users, 'person': person})
    else:
        return render(request, 'patient/profile.html', {'patient': None, 'users': users, 'person': person})


def medsHistory(request):
    person = Person.objects.get(user = User.objects.get(username=request.user))
    patient = Patient.objects.get(person=person)
    prescriptions = Prescription.objects.filter(patient=patient)
    return render(request, 'patient/medicalHistory.html', {
        'person': person, 'prescriptions': prescriptions
    })


