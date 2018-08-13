from django.shortcuts import render
from .models import patient
# Create your views here.
def patient_list(request):
	p = patient.objects.all()
	return render(request, 'patients/patients.html', {'patient': p})
