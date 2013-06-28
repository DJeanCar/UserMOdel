from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
	telefono = models.CharField(max_length=20)
	
