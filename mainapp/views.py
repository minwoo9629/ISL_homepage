from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    if request.user.groups.values().exists():
        user_group = request.user.groups.values()[0]['name']
    else:
        user_group = None
    return render(request,'home.html',{'user_group':user_group})