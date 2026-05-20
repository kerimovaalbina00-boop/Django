from django.db import models
from django.contrib.auth.models import User 


class Profile(models.Model):
    avatar = models.ImageField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

