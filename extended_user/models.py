from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    example_int_value = models.IntegerField(null=True, blank=True)
