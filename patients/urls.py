from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('patientsview/', views.patient_list, name='patient_list'),
]