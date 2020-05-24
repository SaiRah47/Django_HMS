from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from hms.models import Person
from .models import Doctor


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


