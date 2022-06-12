
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    if request.method == 'GET':
        return render(request,'registration/index.html')


class RegisterView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('loginView')
    template_name = 'registration/signup.html'