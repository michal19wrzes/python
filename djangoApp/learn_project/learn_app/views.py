from re import S
from tabnanny import check
from django.shortcuts import render
from learn_app.models import Potrawa,Kucharz
from datetime import datetime


def home(request):
    
    def checkTime(func):
        def wrapper():
            print('e')
            func(2)
            print('el')
        return wrapper
    
    @checkTime
    def something(b):
        if b <1:
            return 0
        if b <2:
            return 1
        else:
            return print('works')
            
            
        
    something()
    
    

    return render(request,'learn_app/index.html')