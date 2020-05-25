from django.shortcuts import render, redirect
from .models import Person
from django.contrib.auth.models import User, Group
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            person = Person.objects.get(user = User.objects.get(username=request.user))
            print(person.type)
            return render(request, 'hms/home.html', {'person': person})
        else:
            return redirect('login')
    else:
        return render(request, 'hms/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        personType = request.POST['personType']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username has already been taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already in use')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    person = Person(user=user)
                    person.type = int(personType)
                    if person.type == 1:
                        p_group = Group.objects.get(name='Patient')
                        p_group.user_set.add(user)
                    else:
                        d_group = Group.objects.get(name='Doctor')
                        d_group.user_set.add(user)
                    person.save()
                    return redirect('login')

        else:
            messages.error(request, 'passwords do not match')
            return redirect('register')
        return redirect('register')
    else:
        return render(request, 'hms/register.html')


def home(request):
    return render(request, 'hms/home.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # messages.success(request,'You are now logged out')
        return redirect('login')
