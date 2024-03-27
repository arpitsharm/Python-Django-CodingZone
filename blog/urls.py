from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('postComment', views.postComment, name="postComment"),
    path('create_post', views.create_post, name="create_post"),
    path('search_post', views.search_post, name="search_post"),
    path('<str:slug>', views.blogpost, name='blogpost'),
]
