from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .serializers import ChoiceSerializer, QuestionSerializer
from rest_framework import generics


from .models import Question, Choice

   
# render - load,fill, and HttpResponse template basing on context variable
# def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {
        # 'latest_question_list':latest_question_list,
    # }
    # return render(request,'polls/index.html',context
    
#REST API 
class ChoiceView(generics.ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer 
    
class QuestionView(generics.ListAPIView): #Create|List
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer



 
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
    

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))   
        
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})   