from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from hms.models import Person
from .models import Doctor, Prescription
from patient.models import Patient
import datetime


def profile(request):
    user = request.user
    user = User.objects.get(username=user)
    person = Person(user=user)
    if request.method == 'POST':
        phone = request.POST['phone']
        gender = request.POST['gender']
        address = request.POST['address']
        age = request.POST['age']
        

        if phone and gender and address and age:
            if Doctor.objects.filter(person=person).exists():
                doctor = Doctor.objects.get(person=person)
                doctor_val = Doctor.objects.filter(person=person).update(person=person, phone=phone, gender=gender, address=address, age=age)
                return redirect('d_profile')

            obj = Doctor.objects.create(person=person, phone=phone, gender=gender, age=age, address=address)
            obj.save()

            return redirect('home')
        else:
            print("Error Occured: ",phone,gender,address,age)
    users = {
        'firstname': request.user.first_name,
        'lastname': request.user.last_name,
        'email': request.user.email,
    }
    print(users)
    doctor = Doctor.objects.filter(person=person)
    if Doctor.objects.filter(person=person).exists():
        doctor = Doctor.objects.filter(person=person)[0]
        return render(request, 'doctor/profile.html', {'doctor': doctor, 'users': users})
    else:
        return render(request, 'doctor/profile.html', {'doctor': None, 'users': users})


def prescription(request):
    if request.method == 'POST':
        patient = request.POST['patient']
        disease = request.POST['disease']
        prescription = request.POST['prescription']
        
        patient_p = Person.objects.get(user=User.objects.get(username=patient))
        doctor_p  = Person.objects.get(user=User.objects.get(username=request.user))
        doc_pres = Prescription(patient=Patient.objects.get(person=patient_p), doctor=Doctor.objects.get(person=doctor_p))
        doc_pres.prescription = prescription
        doc_pres.disease = disease
        doc_pres.date = datetime.datetime.now()
        doc_pres.save()
        return redirect('prescription')
    else: 
        person = Person.objects.get(user=User.objects.get(username=request.user))
        patients = Patient.objects.all()
        prescriptions = Prescription.objects.filter(doctor = Doctor.objects.get(person=person))
        print(person,patients,prescriptions)
        return render(request, 'doctor/prescription.html', {
            'prescriptions': prescriptions,
            'patients': patients,
            'person': person
        })


