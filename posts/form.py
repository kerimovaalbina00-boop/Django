from django.forms import CharField, Form, ImageField, IntegerField, ModelForm

from posts.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "rate", "category", "image"]


class TestForm(Form):
    title = CharField(max_length=255, required=False)
    content = CharField(required=False)
    rate = IntegerField(min_value=1, max_value=10, required=False)
    category = IntegerField(required=False)
    image = ImageField(required=False)