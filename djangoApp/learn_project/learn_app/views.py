from django.shortcuts import render
from learn_app.models import Potrawa,Kucharz
from learn_app.serializers import KucharzSerializer,PotrawaSerializer
from datetime import datetime
from rest_framework import generics


class KucharzList(generics.ListCreateAPIView):
    queryset = Kucharz.objects.all()
    serializer_class = KucharzSerializer
    
class PotrawaList(generics.ListCreateAPIView):
    queryset = Potrawa.objects.all()
    serializer_class = PotrawaSerializer
    

def home(request):
    
    def checkTime(func):
        def wrapper():
            n= datetime.now()
            func(6)
            n = datetime.now()-n
            print(f'Czas trwania programu: {n}')
        return wrapper
    
    @checkTime
    def something(b):
        if b <1:
            return 0
        if b <2:
            return 1
        else:
            return print(something(b-2)+something(b-1))
            
            
        
    
    
    

    return render(request,'learn_app/index.html')