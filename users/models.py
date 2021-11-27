from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
