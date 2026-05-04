from django.contrib.auth.models import User
from django.db import models

# CREATE TABLE IF NOT EXISTS ...
# class Model(models.Model): ...

# SELECT * FROM posts

# modelname.objects.all()

# SELECT * FROM posts WHERE ...

# modelname.objects.filter()

# UPDATE model SET id = 2

# modelname.title = 12300
# modelname.save()

# modelname.objects.get(id=1)
# modelname.delete()
# modelname.save()


# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=255)

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Tag(models.Model):
    title = models.CharField(max_length=255)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    rate = models.IntegerField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="posts", null=True, blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )

    tags = models.ManyToManyField(Tag, null=True, blank=True)
    

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = "Posts"
        verbose_name_plural = "Post"


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"

    def __str__(self) -> str:
        return f"{self.name}"

