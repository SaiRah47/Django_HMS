from django.urls import path, include
from . import views

urlpatterns = [
    path('profile',views.profile,name='p_profile'),
    path('history',views.medsHistory,name='history')
]