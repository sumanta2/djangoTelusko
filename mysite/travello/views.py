from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination


def index(request):

    dests= Destination.objects.all()   #it fetch all data present in postgreSql database's Destination table

    
    return render(request,'index.html',{'dests':dests})