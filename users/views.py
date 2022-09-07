from multiprocessing import context
from venv import create
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views import View
from plantas.models import Plant
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def userRegister(request):
    username = request.POST.get('username')
    password= request.POST.get('password')
    db = get_user_model()
    try:
        db.objects.create_user(username=username, password=password)
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('myaccount')
    except Exception:
        return redirect('/?status=1')


def userAuthenticate(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user==None:
        return redirect('/?status=2')
    else:
        login (request, user)
        return redirect('myaccount')

class MainPage(LoginRequiredMixin,View):
    login_url='/'
    def get(self,request):
        ultimasComu = Plant.objects.all().order_by('-last_modf')[:9]
        ultimasVc = Plant.objects.filter(contributor=request.user).order_by('-last_modf')[:4]
        context = {
            'ultimas': ultimasComu,
            'ultimasVc': ultimasVc,
        }
        return render(request, 'mainpage.html', context)
    def post(self,request):
        pass

class Comunidade(LoginRequiredMixin,View):
    login_url = '/'
    def get(self,request):
        plantas = Plant.objects.all()
        context = {
            'plantas': plantas,
        }
        return render(request, 'comunidade.html', context)
    def post(self,request):
        pass

@login_required(login_url='/')
def exit(request):
    logout(request)
    return redirect('home')