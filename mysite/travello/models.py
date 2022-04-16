from django.db import models
#from pyparsing import srange

# Create your models here.

class Destination(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

    #convert normal class to python model which automatically create table in postgreSql and also create a web layout in admin panel