from django.db import models

class Application(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    education = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10, default='')
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
