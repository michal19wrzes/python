
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
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

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('loginView')
    template_name = 'registration/signup.html'