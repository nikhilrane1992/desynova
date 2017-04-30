from django.db import models

class ShortUrl(models.Model):
	short_url_string = models.CharField(max_length=100, unique=True)
	original_url = models.CharField(max_length=100)

class PasteLockly(models.Model):
	short_url_string = models.CharField(max_length=100, unique=True)
	secret_key = models.CharField(max_length=100)
	content = models.TextField()