from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.db.models.aggregates import Sum
from .models import Expense
from user import models
from user import forms
from .forms import ContactForm
from django.contrib import messages

from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Expense
def custom_logout(request):
    logout(request)
    return redirect('login')









def main_page(request):
    return render(request, 'main/main.html')

def contactus(request):
    return render(request, 'main/contactus.html')


def index(request):
    return render(request, 'main/index.html')


def aboutus(request):
    return render(request, 'main/aboutus.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('contactus')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ContactForm()
    return render(request, 'main/contactus.html', {'form': form})


