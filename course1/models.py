from django.db import models

# Create your models here.
class file_upload(models.Model):
	ids = models.AutoField(primary_key=True)
	file_name = models.CharField(max_length=255)
	my_file = models.FileField(upload_to='')
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.file_name