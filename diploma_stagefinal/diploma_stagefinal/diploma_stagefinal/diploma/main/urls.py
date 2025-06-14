from django.contrib import admin
from django.urls import path
from main import views
from .views import *

urlpatterns = [
    path('logout/', views.custom_logout, name="logout"),
    
   
    path('index/', views.index, name='index'),
    
    path('aboutus/', views.aboutus, name='aboutus'),
    path('', views.main_page,name='main'),
    path('contactus/', views.contact_us,name='contactus'),

    
]



