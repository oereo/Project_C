from django.shortcuts import render, redirect
from django.contrib import auth
# Create your views here.
def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        print('log out success')
        return redirect('/')
    return render(request,'index.html')