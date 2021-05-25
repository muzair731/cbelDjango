from django.db import models

# Create your models here.
class sendemail(models.Model):
	email = models.EmailField()
	subject = models.CharField(max_length=255)
	message = models.TextField()