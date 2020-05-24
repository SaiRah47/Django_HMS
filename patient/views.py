from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from hms.models import Person
from .models import Patient


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
            if Patient.objects.filter(person=person).exists():
                # print("hello")
                patient = Patient.objects.get(person=person)
                patient_val = Patient.objects.filter(person=person).update(person=person, phone=phone, gender=gender, address=address, age=age)
                # print("created")
                return redirect('p_profile')

            obj = Patient.objects.create(person=person, phone=phone, gender=gender, age=age, address=address)
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
    patient = Patient.objects.filter(person=person)
    if Patient.objects.filter(person=person).exists():
        patient = Patient.objects.filter(person=person)[0]
        return render(request, 'patient/profile.html', {'patient': patient, 'users': users})
    else:
        return render(request, 'patient/profile.html', {'patient': None, 'users': users})


