from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    display_name = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank=True)

