from django.db import models

class patient(models.Model):
	Reg_No     = models.CharField(max_length=20)
	first_name = models.CharField(max_length=25)
	Last_name  = models.CharField(max_length=25)
	Email      = models.EmailField(max_length=50)
	Patient_Age = models.CharField(max_length=10)
	Gender = models.CharField(max_length=10)
	Patient_Address = models.TextField(max_length=200)
	Contact = models.CharField(max_length=50)
	Room = models.CharField(max_length=10)
	date = models.DateTimeField(auto_now_add=False)


def __str__(self):
	return ' '.join([
		self.first_name,
		self.Last_name,
		])