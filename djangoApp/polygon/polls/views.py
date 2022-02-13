from django.shortcuts import render
from django.http import HttpResponse

from .models import Question
   
# render - load,fill, and HttpResponse template basing on context variable
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':latest_question_list,
    }
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    return HttpResponse("You are looking at question %s."%question_id)
    
def results(request,question_id):
    return HttpResponse("You are looking at the results of question %s."%question_id)
    
def vote(request,question_id):
    return HttpResponse("You are looking at the vote of question %s."%question_id)
    
    