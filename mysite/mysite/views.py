from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Hello, world. You're at the Django index.<h2>")

def renderMe(request):
    return render(request,'home.html',{'name':'SUMANTA'})

def add(request):
    '''val1=int(request.GET['num1'])   for get request
    val2=int(request.GET['num2'])'''

    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    result=val1+val2
    return render(request,'result.html',{'result':result})