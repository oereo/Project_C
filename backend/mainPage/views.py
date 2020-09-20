from django.shortcuts import render, redirect
from django.contrib import auth
from account.models import User
from django.contrib.auth import models, views, login
from .models import Profile, Area


# for webCrawling 
from bs4 import BeautifulSoup as BS
import random
import json
import requests

# Create your views here.
def index(request):
    url = 'http://www.weather.go.kr/weather/observation/currentweather.jsp'
    response = requests.get(url)

    if(response.status_code != 200):
        print("%d error" % response.status_code)
        quit()

    soup = BS(response.content, 'html.parser')
    table = soup.find('table', {'class': 'table_develop3'})

    data_temp = []
    point_temp = []
    for tr in table.find_all('tr'):
        tds = list(tr.find_all('td'))
        for td in tds:
            if td.find('a'):
                point = td.find('a').text
                rain = tds[8].text
                wind_dir = tds[10].text 
                wind_speed = tds[11].text
                temperature = tds[5].text
                humidity = tds[9].text
                point_temp.append(point)
                data_temp.append([point, temperature, humidity, rain, wind_dir, wind_speed])
    length = len(data_temp)
    return render(request, "index.html", {'data_temp':data_temp, 'point_temp':point_temp, 'length' : length})

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
                phone_number = request.POST['phone_number'],
                password = request.POST['password'],
                email = request.POST['email'],
                nickname = request.POST['nickname'],
                date_of_birth = request.POST['date_of_birth'],
                #seller_address = request.POST['seller_address'],
                business_number = request.POST['business_number'],
                team = request.POST['team'],
            )
            auth.login(request, user)

        return redirect('index')
        
    else:
        #form = UserCreationForm()
        return render(request, 'register.html')

def profile_update(request):
    if request.method == "POST":
        profile = Profile()
        profile.user = request.user
        profile.worker_number = request.POST['worker_number']
        profile.instrument_number = request.POST['instrument_number']
        profile.safe_percent = request.POST['safe_percent']
        worker_number = profile.worker_number
        instrument_number = profile.instrument_number
        safe_percent = profile.safe_percent
        profile.save()
        return render(request, 'profile.html', {'worker_number' : worker_number, 'instrument_number' : instrument_number, 'safe_percent': safe_percent})


def pick_instrument(request, instrument_id):
    pick_instrument = Area.objects.get(pk = instrument_id)#Poll객체를 구분하는 녀석은 poll_id이므로 PK지정
    #selection = request.POST['choice']
 
    try:
        #choice모델을 불러와서 1을 증가시킨다 
        #choice = Choice.objects.get(instrument_id = pick_instrument.id)
        # choice.votes += 1
        choice.save()
    except:
        choice = Area(instrument_id = pick_instrument.id)
        choice.save()
    return redirect('icons') 

def save_instrument(request):
    Area.areaUser = request.user
    Area.measuringInstrument = Instrument.objects.filter(instrument = "ab51d3 계측기")
    Area.save() 
    return render(request, 'icons')



