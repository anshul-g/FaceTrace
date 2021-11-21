from django.contrib.auth.models import AbstractUser,User
from django.conf import settings
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    Institution = models.CharField("Institution", max_length=100)

    def __str__(self):
        return self.email