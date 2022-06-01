from urllib import response
from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request,'index.html')
        