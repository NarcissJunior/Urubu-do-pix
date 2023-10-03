from django.shortcuts import render
from .models import User

def home (request):
    user = User.objects.all()
    return user
