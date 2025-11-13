from django.db import models

# Create your models here.
class Members(models.Model):
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	email = models.EmailField(unique=True)
	mobile = models.CharField(max_length=13,unique=True)
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.firstname + " " + self.lastname
