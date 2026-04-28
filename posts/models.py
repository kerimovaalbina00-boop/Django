from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    rate = models.IntegerField()


class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

