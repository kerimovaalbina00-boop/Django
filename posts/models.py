from django.db import models
from django.contrib.auth.models import User

"""
posts = Post.objects.all()
posts = Post.objects.get(id=1) только универсальное значение
posts = Post.objects.filter()
"""
"""
Post.objects.create(
    name="Название поста",
    content="Контент поста",
    rate=5,
)
"""


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1000, null=True, blank=True)
    rate = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    # связи
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title} - {self.content}"
    
class Comment(models.Model):
    content = models.CharField(max_length=500)

    # связи
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.content}"


