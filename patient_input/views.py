from django.shortcuts import render
from .forms import PatientInput
from patients.models import patient

def home(request):
	if request.method == 'POST':
		form = PatientInput(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			patient.objects.create(**form.cleaned_data)
	else:
		form = PatientInput()
	return render(request, 'patient_input/home.html', {'form': form})