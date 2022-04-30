from django.shortcuts import render
from learn_app.models import Potrawa,Kucharz
from datetime import datetime

# Create your views here.
def home(request):
    n = datetime.now()
    
    kucharz_potrawa = Kucharz.objects.prefetch_related('potrawa_set').all()
    
    potrawa_kucharz = Potrawa.objects.select_related('powi').all()

    for kucharz in kucharz_potrawa:
        # print(kucharz.__dict__)
        potrawy = kucharz.potrawa_set.all()
        print(str([(potrawa.smak) for potrawa in potrawy]))

    # for potrawa in potrawy:
    #     print(potrawa.powi.age)

    p = datetime.now() - n
    print(p)

    return render(request,'learn_app/index.html')