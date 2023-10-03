from django.http import HttpResponse
from django.shortcuts import render
from .models import UserModel


def home(request):
    user = UserModel.objects.all()
    return user

def user(request, user_id):
    return HttpResponse("User id: %s" % user_id)
