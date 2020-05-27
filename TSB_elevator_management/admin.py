from django.contrib import admin
from .models import TSBCity, Elevator

admin.site.register([TSBCity, Elevator])