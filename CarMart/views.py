from django.shortcuts import render , get_object_or_404
from  Brand.models import *


def home(request,id=None):

    if id is not None:
        brands = get_object_or_404(brand, id=id) 
        car = Car.objects.filter(brand=brands) 
            
            
    else:
        car=Car.objects.all()
        
    brands = brand.objects.all()
    return render (request,'home.html',{"brands":brands,"Car":car})
    
    
