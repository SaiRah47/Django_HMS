from django.shortcuts import render
from .models import Appointment
from hms.models import Person
from django.contrib.auth.models import User

# Create your views here.
def appointment(request):
    person = Person.objects.get(user=User.objects.get(username=request.user))
    appointments = Appointment(patient=Patient.objects.filter(person=person))
    return render(request, 'patient/appointments.html', {'appointments': appointments, 'person': person})
