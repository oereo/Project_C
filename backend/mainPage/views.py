from django.shortcuts import render, redirect
from django.contrib import auth
from account.models import User
from django.contrib.auth import models, views, login


# for webCrawling 
from bs4 import BeautifulSoup as BS
import random
import json
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def icons(request):
    return render(request, 'icons.html')
def loginp(request):
    return render(request, 'login.html')
def map(request):
    return render(request, 'map.html')
def maps(request):
    return render(request, 'maps.html')
def profile(request):
    return render(request, 'profile.html')
def register(request):
    return render(request, 'register.html')
def tables(request):
    return render(request, 'tables.html')
def upgrade(request):
    return render(request, 'upgrade.html')

def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email = email, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def signup_user(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password_confirm']:
            user = User.objects.create_bussiness_user(
                # request.POST['email'],
                phone_number = request.POST['phonenumber'],
                password = request.POST['password'],
                email = request.POST['username'],
                nickname = request.POST['nickname'],
                date_of_birth = request.POST['dateofbirth'],
                #seller_address = request.POST['seller_address'],
                business_number = request.POST['business_number'],
                team = request.POST['team'],
            )
            auth.login(request, user)

        return redirect('home')
        
    else:
        #form = UserCreationForm()
        return render(request, 'register.html')


def Crawling(request):
    url = 'http://www.weather.go.kr/weather/observation/currentweather.jsp'