from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination


def index(request):
    dest1=Destination()
    dest1.name='Mumbai'
    dest1.price=700
    dest1.img="destination_1.jpg"
    dest1.desc="The city That Never Sleeps"

    dest2=Destination()
    dest2.name='Hydrabad'
    dest2.price=650
    dest2.img="destination_2.jpg"
    dest2.desc="First Biriyani, Then Sherwani"

    dest3=Destination()
    dest3.name='Bengaluru'
    dest3.price=750
    dest3.img="destination_3.jpg"
    dest3.desc="Beautiful City"   

    dests= [dest1,dest2,dest3]
    print(dests[0].name)
    return render(request,'index.html',{'dests':dests})