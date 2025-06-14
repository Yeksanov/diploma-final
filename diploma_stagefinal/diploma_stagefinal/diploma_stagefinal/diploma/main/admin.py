from django.contrib import admin
from .models import *
from django.db.models import Sum
from .models import ContactMessage

admin.site.register(ContactMessage)