from django.shortcuts import render
from learn_app.models import Potrawa,Kucharz
from datetime import datetime

# Create your views here.
def home(request):
    n = datetime.now()
    
    
    def testDecorator(func):
        def wrapper():
            print('before')
            func()
            print('after')
        return wrapper
        
    @testDecorator
    def testDef():
        print('testDef')

    testDef()

    p = datetime.now() - n
    print(p)

    return render(request,'learn_app/index.html')