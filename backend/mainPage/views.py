from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def icons(request):
    return render(request, 'icons.html')
def login(request):
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
