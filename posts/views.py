from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint
from posts.models import Post, Comment
from posts.forms import CommentForm, PostCrateForm, PostModelForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import ListView



def test_view(request):
    return HttpResponse(f"This is a test view {randint(1, 1000)}")

def html_view(request):
    return render(request, "base.html")

class ListViewClass(ListView):
    def get(self, request): 
        posts = Post.objects.all()
        limited_posts = 5
        if request.method == "GET":
            form = SearchForm(request.GET)
            search = request.GET.get("search")
            category_id = request.GET.get("category_id")
            tags_ids = request.GET.getlist("tags_ids")
            orderings = request.GET.get("orderings")
            page = int(request.GET.get("page", 1)) if request.GET.get("page") else 1
            if search:
                posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
            if category_id:
                posts = posts.filter(category=category_id)
            if tags_ids:
                posts = posts.filter(tags__id__in=tags_ids).distinct()
            if orderings:
                posts = posts.order_by(orderings)

            post_count = posts.count()
            insufficient_posts = post_count % limited_posts
            max_page = post_count / limited_posts if (insufficient_posts == 0) else (post_count // limited_posts) + 1
            start_page = (page-1) * limited_posts
            end_page = start_page + limited_posts
            posts = posts[start_page:end_page]
            return render(request, "post/list_view.html", context={"posts": posts, "form": form, "max_page": range(1, int(max_page + 1))})
        

@login_required(login_url='/login/') 
def post_detail_view(request, post_id):
    if request.method == "GET":
        posts = Post.objects.filter(id=post_id).first()
        comment = CommentForm()
        comment_for_model = Comment.objects.filter(post_id=post_id)
        if not posts:
            return redirect("/list_view/")
        return render(request, "post/post_detail.html", context={"post": posts, "comment": comment , "comment_for_model": comment_for_model})
    if request.method == "POST":
        form = CommentForm(request.POST)
        posts = Post.objects.filter(id=post_id).first()
        comment_for_model = Comment.objects.filter(post_id=post_id)
        if form.is_valid():
            comment = form.cleaned_data.get("content")
            Comment.objects.create(
                content=comment,
                post=posts,
            )
            return render(request, "post/post_detail.html", context={"post": posts, "comment": comment , "comment_for_model": comment_for_model})
        return redirect(f"/list_view/{post_id}/")

@login_required(login_url='/login/') 
def create_post_view(request):
    if request.method == "POST":
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data.get("image"),
                title=form.cleaned_data.get("title"),
                content=form.cleaned_data.get("content"),
                rate=form.cleaned_data.get("rate"),
            )
        else:
            return render(request, "post/create_post.html", context={"form": form})
        return redirect("/list_view/")
    if request.method == "GET":
        return render(request, "post/create_post.html")

