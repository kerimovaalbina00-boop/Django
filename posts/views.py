# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from posts.models import Post


def home(request):
    post = Post.objects.get(id=1)
    return HttpResponse(f"<h1>Text</h1>  ---- {post.title} <br> {post.content}")



def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

