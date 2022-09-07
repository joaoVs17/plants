from __future__ import absolute_import
from email import message
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Plant
from django.utils import timezone
from django.contrib import messages

# Create your views here.

class MyPlants(LoginRequiredMixin,View):
    login_url = '/'
    redirect_field_name = 'home'
    def get(self,request):
        status = request.GET.get('status')
        plantas = Plant.objects.all()
        context = {
            'plantas':plantas,
            'status': status
        }
        return render(request, 'myplants.html', context)
    def post(self, request):
        pass

class Add(LoginRequiredMixin, View):
    login_url = '/'
    def get(self,request):
        return render(request,'cadastroplantas.html')
    def post(self,request):
        nome = request.POST.get('nome')
        cientifico = request.POST.get('cientifico')
        origem = request.POST.get('origem')
        url = request.POST.get('url')
        sobre = request.POST.get('sobre')
        if (len(Plant.objects.filter(scientific_name=cientifico))<1):
            try:
                Plant.objects.create(name=nome,scientific_name=cientifico,origin=origem,image_url=url,about=sobre,contributor=request.user)
                return redirect('/myaccount/myplants/?status=0')
            except Exception:
                return redirect('/myaccount/myplants/?status=1')
        else:
            return redirect('/myaccount/myplants/?status=2')

@login_required(login_url='/')
def deletePlant(request,pk):
    planta = Plant.objects.get(pk=pk)
    planta.delete()
    return redirect('myplants')

@login_required(login_url='/')
def editPlant(request,pk):
    planta = Plant.objects.get(pk=pk)
    if request.method == 'GET':
        nome = planta.name
        cientifico = planta.scientific_name
        origem = planta.origin
        url = planta.image_url
        sobre = planta.about
        context = {
            'nome':nome,
            'cientifico':cientifico,
            'origem': origem,
            'url': url,
            'sobre':sobre,
        }
        return render(request, 'editarplanta.html', context)
    if request.method == 'POST':
        planta.name = request.POST.get('nome')
        planta.scientific_name = request.POST.get('cientifico')
        planta.origin = request.POST.get('origem')
        planta.image_url = request.POST.get('url')
        planta.about = request.POST.get('sobre')
        planta.save()
        return redirect('myplants')
    