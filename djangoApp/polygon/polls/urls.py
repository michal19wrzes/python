from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('',views.index,name='index'),
    path('api/choice',views.ChoiceView.as_view()),
    path('api/question',views.QuestionView.as_view()),
    path('<int:question_id>/results/',views.results,name='results'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
]