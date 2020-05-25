from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.patients, name='rpatients'),
    path('delete_patient/<int:patient_id>', views.delete_patient, name='delete_patient'),
    path('update_patient/<int:patient_id>',views.update_patient, name='update_patient')
]


