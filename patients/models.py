from django.db import models
from hms.models import Receptionist

class Recep_patient(models.Model):
    receptionist = models.ForeignKey(Receptionist, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default=None)
    phone = models.CharField(max_length=10, default=None)
    email = models.CharField(max_length=100, default=None)
    gender = models.CharField(max_length=10, default=None)
    age = models.IntegerField(default=None)

    def __str__(self):
        return self.receptionist.person.user.username
