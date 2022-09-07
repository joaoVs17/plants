from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import View


# Create your views here.

def home(request):
        if request.user.is_authenticated:
                return redirect('myaccount')
        else:
                status = request.GET.get('status')
                context = {
                        'status': status,
                }
                return render(request, 'home.html', context)

def sobre(request):
        if request.user.is_authenticated:
                return redirect('myaccount')
        else:
                return render(request, 'sobre.html')