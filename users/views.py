# Create your views here.

from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from users.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from posts.models import Post, Comment
from posts.forms import PostModelForm

from users.models import Profile

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', context={'form': form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'users/register.html', context={'form': form})
        form.cleaned_data.__delitem__('confirm_password')
        avatar = form.cleaned_data.pop('avatar')
        age = form.cleaned_data.pop('age')
        user = User.objects.create_user(**form.cleaned_data)
        if user:
            Profile.objects.create(user=user, avatar=avatar, age=age)
        return redirect('/')
    
def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html', context={'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'users/login.html', context={'form': form})
        user = authenticate(**form.cleaned_data)
        if user:
            login(request, user)
        return redirect('/')
    
def logut(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/') 
def profile_view(request):
    if request.method == 'GET':
        user = request.user
        profile = user.profile
        users_posts = Post.objects.filter(author=user)
        if profile:
            return render(request, 'users/profile.html', context={'user': user, 'profile': profile, 'users_posts': users_posts})
        else:
            return redirect('/')
    

@login_required(login_url='/login/') 
def update_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid() and post.author == request.user:
            form.save()
        return redirect('/profile/')
    elif request.method == 'GET':
        form = PostModelForm(instance=post)
        comments = Comment.objects.filter(post=post)
        return render(request, 'users/update_post.html', context={'post': post, 'form': form, 'comment_for_model': comments})