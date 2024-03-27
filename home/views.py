from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone_number = request.POST['phone_num']
        message = request.POST['message']

        if name == '' or email == '' or subject == '' or phone_number == '' or message == '':
            messages.error(request, "Please fill all the fields")

        else:
            contact = ContactUs(name=name, email=email, subject=subject, phone_num=phone_number, message=message)
            contact.save()
            messages.success(request, "Successfully Contact Add")        
        return redirect('contact')
    
    return render(request, 'contact.html')


def loginpage(request):
    return render(request, 'login.html')

def registerpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        lastname = request.POST['lastname']
        email_add = request.POST['emailadd']
        password = request.POST['password']
        con_password = request.POST['con_password']

        if username == '' or first_name == '' or lastname == '' or email_add == '' or password == '' or con_password == '':
            messages.error(request, "Please fill all the fields")
            
        elif password!= con_password:
            messages.error(request, "Passwords do not match")

        else:
            data = User(username=username, first_name=first_name, last_name=lastname, password=password)
            data.save()

    return render(request, 'register.html')

def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")


def logoutpage(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect("home")

def apps(request):
    return render(request, 'apps.html')


def use_apps(request):
    allApps = Apps.objects.all()
    context = {"apps": allApps}
    return render(request, 'use_apps.html', context)

def create_apps(request):
    if request.method == 'POST':
        app_name=request.POST['app_name']
        app_file_name=request.POST['app_file_name']
        app_icon=request.POST['select_app_icon']

        data = Apps(name=app_name, file=app_file_name, image=app_icon)
        data.save()

        messages.success(request, "Successfully App Add")


    return render(request, 'create_app.html')

def apps_file(request, cmd):
    return render(request, f'{cmd}.html')
