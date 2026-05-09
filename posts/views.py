from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from posts.form import TestForm
from posts.models import Category, Post
from posts.posts import get_posts_filter_by_rate


def get_posts_by_category(request, id):
    posts = Post.objects.filter(category_id=id)

    return render(
        request,
        "posts/posts.html",
        context={"posts": posts},
    )


def create_post(request: HttpRequest):

    categories = Category.objects.all()

    if request.method == "POST":
        form = TestForm(request.POST, request.FILES)

        if form.is_valid():
            cleaned_data = form.cleaned_data

            Post.objects.create(
                title=cleaned_data["title"],
                content=cleaned_data["content"],
                rate=cleaned_data["rate"],
                image=cleaned_data.get("image"),
                category_id=cleaned_data["category"],
            )

            return redirect("posts")

        return render(
            request,
            "posts/create_post.html",
            context={
                "form": form,
                "categories": categories,
                "errors": form.errors,
            },
        )

    form = TestForm()

    return render(
        request,
        "posts/create_post.html",
        context={
            "form": form,
            "categories": categories,
        },
    )


def edit_post(request: HttpRequest, pk):

    post = get_object_or_404(Post, id=pk)
    categories = Category.objects.all()

    if request.method == "POST":
        form = TestForm(request.POST, request.FILES)

        if form.is_valid():
            cleaned_data = form.cleaned_data

            post.title = cleaned_data["title"]
            post.content = cleaned_data["content"]
            post.rate = cleaned_data["rate"]

            if cleaned_data.get("image"):
                post.image = cleaned_data["image"]

            post.category_id = cleaned_data["category"]

            post.save()

            return redirect("post", id=post.pk)

        return render(
            request,
            "posts/edit_post.html",
            context={
                "post": post,
                "categories": categories,
                "errors": form.errors,
            },
        )

    return render(
        request,
        "posts/edit_post.html",
        context={
            "post": post,
            "categories": categories,
        },
    )


def delete_post(request: HttpRequest, id):

    post = get_object_or_404(Post, id=id)

    if request.method == "GET":
        post.delete()

        return redirect("posts")
    

def create_category(request: HttpRequest):
    if request.method == "POST":
        name = request.POST.get("name")

        if name:
            Category.objects.create(name=name)

            return redirect("home")

    return render(request, "posts/create_category.html")

