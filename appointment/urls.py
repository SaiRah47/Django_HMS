from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment, name='appointment'),
    path('patient', views.p_appointment, name='p_appointment'),
    path('doctor', views.d_appointment, name='d_appointment'),
    path('change/<int:appointment_id>', views.change_appointment, name='change_appointment'),
    path('update',views.updateAppointment, name='update'),
    path('delete/<int:appointment_id>', views.delete_appointment, name='delete_appointment'),
]