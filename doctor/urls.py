from django.urls import path, include
from . import views

urlpatterns = [
    path('profile',views.profile,name='d_profile'),
    path('prescription',views.prescription,name="prescription")
]