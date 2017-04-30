from django.db import models

class Short_url(models.Model):
	short_random_string = models.CharField(max_lenght=100, unique=True)
	original_url = models.CharField(max_lenght=100)