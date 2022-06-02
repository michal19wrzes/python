from urllib import response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request,'index.html')

# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         #irect to a success page.
#         return render(request,'/auth/success')
#     else:
#         return render(request,'index.html')