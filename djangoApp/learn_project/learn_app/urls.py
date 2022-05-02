from learn_app import views
from django.urls import path, include

urlpatterns = [

    path('',views.home, name='home' ),
    path('asd/',views.KucharzList.as_view(), name='generic1' ),
    path('dsa/',views.PotrawaList.as_view(), name='generic2' ),
]
