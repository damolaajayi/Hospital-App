from django import forms

class PatientInput(forms.Form):
	Reg_No = 			forms.CharField(max_length=30)
	first_name	= 		forms.CharField(max_length=100)
	Last_name	=		forms.CharField(max_length=100)
	Email = 	forms.EmailField(max_length=100)
	Patient_Age = 		forms.CharField(max_length=30)
	Gender = 			forms.CharField(max_length=30)
	Patient_Address = 	forms.CharField(max_length=250)
	Contact = 			forms.CharField(max_length=250)
	Room = 				forms.CharField(max_length=30)
	date = 				forms.CharField(max_length=30)


def clean(self):
	cleaned_data = super(PatientInput, self)
	Reg_No = cleaned_data.get('Reg No')
	first_Name = cleaned_data.get('First Name')
	Last_Name = cleaned_data.get('Last Name')
	Email = cleaned_data.get('Email')
	Patient_Age = cleaned_data.get('Patient Age')
	Gender = cleaned_data.get('Gender')
	Patient_Address = cleaned_data.get('Patient	Address')
	Contact = cleaned_data.get('Contact')
	Room = cleaned_data.get('Room')
	date = cleaned_data.get('Date')