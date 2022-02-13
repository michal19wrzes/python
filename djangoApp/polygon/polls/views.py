from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404


from .models import Question
   
# render - load,fill, and HttpResponse template basing on context variable
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':latest_question_list,
    }
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    try:
        question = get_object_or_404(Question,pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
   
    return render(request,'polls/detail.html',{'question':question})
    
def results(request,question_id):
    return HttpResponse("You are looking at the results of question %s."%question_id)
    
def vote(request,question_id):
    return HttpResponse("You are looking at the vote of question %s."%question_id)
    
    