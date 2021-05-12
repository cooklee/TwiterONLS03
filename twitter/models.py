from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Tweet(models.Model):
    content = models.CharField(max_length=256)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
