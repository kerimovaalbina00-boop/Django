"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from posts.views import test_view, html_view, ListViewClass, post_detail_view, create_post_view
from users.views import login_view, logut, register_view, profile_view, update_post_view
from django.conf import settings
from django.conf.urls.static import static

users_paterns = [
    path('register/', register_view), 
    path('login/', login_view), 
    path('logout/', logut),
    path('profile/', profile_view), 
    path('profile/list_view/update/<int:post_id>/', update_post_view), 
    ]

urlpatterns = users_paterns + [
    path('admin/', admin.site.urls),
    path("", html_view),
    path("list_view/", login_required(ListViewClass.as_view(), login_url='/login/')), 
    path("list_view/<int:post_id>", post_detail_view), 
    path("list_view/create/", create_post_view), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

