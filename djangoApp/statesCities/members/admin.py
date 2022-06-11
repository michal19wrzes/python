from django.contrib import admin

from members.models import UserAccount
from .models import UserAccount
# Register your models here.
admin.site.register(UserAccount)