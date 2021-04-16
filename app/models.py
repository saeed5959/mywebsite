from django.db import models

# Create your models here.
class user_info(models.Model):
    username = models.CharField(max_length=45)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.EmailField()
