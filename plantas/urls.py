from django.urls import path
from . import views

urlpatterns = [
    path('myaccount/myplants/', views.MyPlants.as_view(), name='myplants'),
    path('myaccount/myplants/add/', views.Add.as_view(), name='addPlanta'),
    path('myaccount/myplants/delete/<int:pk>', views.deletePlant, name='delPlant'),
    path('myaccount/myplants/edit/<int:pk>', views.editPlant, name='editPlant'),
]
