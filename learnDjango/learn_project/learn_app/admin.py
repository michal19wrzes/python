from django.contrib import admin

# Register your models here.
from learn_app.models import Kucharz,Potrawa
class KucharzAdmin(admin.ModelAdmin):
    pass
admin.site.register(Kucharz, KucharzAdmin)
admin.site.register(Potrawa, KucharzAdmin)
