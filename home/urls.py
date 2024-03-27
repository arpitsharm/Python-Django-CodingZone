from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('registerpage', views.registerpage, name='registerpage'),
    path('handleLogin', views.handleLogin, name='handleLogin'),
    path('logoutpage', views.logoutpage, name='logoutpage'),
    path('apps', views.apps, name='apps'),
    path('use_apps', views.use_apps, name='use_apps'),
    path('create_apps', views.create_apps, name='create_apps'),
    path('<str:cmd>', views.apps_file, name='apps_file'),
]
