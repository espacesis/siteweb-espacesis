from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    number_phone = models.CharField(max_length=255, default="")
