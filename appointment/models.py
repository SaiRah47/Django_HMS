from django.db import models
from hms.models import Person, Receptionist
from patient.models import Patient
from doctor.models import Doctor

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    receptionist = models.ForeignKey(Receptionist, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    choices = [("pending", "pending"), ("completed", "completed")]
    status = models.CharField(choices=choices, max_length=256, default="pending")

    def __str__(self):
        return self.patient.person.user.username + ' appointment with ' + self.doctor.person.user.username
    
