from django.db import models

# Create your models here.
class List(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.item + ' ' + str(self.completed)

		