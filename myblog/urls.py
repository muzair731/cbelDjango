"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from . import views
from .views import blog_content, blog_detail, blog_add, blog_update, blog_comment

urlpatterns = [
    #path('blog_content/',views.blog_content, name="blog_content"),
    path('blog_content/', blog_content.as_view(), name = 'blog_content'),
    path('blog_detail/<int:pk>/', blog_detail.as_view(), name = 'blog_detail'),
    path('blog_add/',blog_add.as_view(), name = 'blog_add'),
    path('blog_detail/edit/<int:pk>', blog_update.as_view(), name = 'blog_update'),
    path('blog_detail/<int:pk>/comment',blog_comment.as_view(), name = 'blog_comment'),
]