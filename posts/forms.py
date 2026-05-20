from django import forms
from posts.models import Category, Post, Tag


class PostCreateForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField(max_length=255)
    content = forms.CharField(max_length=1000)
    rate = forms.IntegerField(min_value=0, max_value=10)

    def clean_post(self):
        clean_data = super().clean()
        title = clean_data.get("title")
        content = clean_data.get("content")
        if not title and not content:
            raise forms.ValidationError("Заполните все поля")
        if title == content:
            raise forms.ValidationError("Тайтл не должен быть равен контенту")
        return clean_data
    
class PostModelForm(forms.ModelForm):
    class Meta:
            model = Post
            fields = ["image", "title", "content", "rate"]

class CommentForm(forms.Form):
    content = forms.CharField(max_length=500)

    def clean_content(self):
        clean_data = super().clean()
        content = clean_data.get("content")
        return content
    
class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    tags_ids = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    orderings = (
        ("rate", "По рейтингу по возрастанию"),
        ("-rate", "По рейтингу по убыванию"),
        ("title", "По названию по возрастанию"),
        ("-title", "По названию по убыванию"),
        (None, "Без сортировки"),
    )
    orderings = forms.ChoiceField(choices=orderings, required=False)

    def clean_search(self):
        clean_data = super().clean()
        return clean_data