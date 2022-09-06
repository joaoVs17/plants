from django.shortcuts import render, redirect
from django.views import View


# Create your views here.

def home(request):
        if request.user.is_authenticated:
                return redirect('myaccount')
        else:
                return render(request, 'home.html')

def sobre(request):
        if request.user.is_authenticated:
                return redirect('myaccount')
        else:
                return render(request, 'sobre.html')