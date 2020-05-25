from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment, name='appointment'),
    path('patient', views.p_appointment, name='p_appointment'),
    path('doctor', views.d_appointment, name='d_appointment'),
]