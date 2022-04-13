from django.db import models
#from pyparsing import srange

# Create your models here.

class Destination:
    id:int
    name:str
    img:str
    price:int
    offer:bool