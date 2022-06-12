
from django.contrib import admin
from django.db import router
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework import routers
from members.views import UserAccountViewSet

router = routers.DefaultRouter()
router.register(r'users',UserAccountViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('members.urls')),
    path('auth-api/',include('rest_framework.urls')),
    path('auth-api/',include(router.urls)),

    #path('', TemplateView.as_view(template_name = 'index.html')),
]
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
