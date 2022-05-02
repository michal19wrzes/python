import factory
from factory import fuzzy
from .models import Potrawa,Kucharz

class KucharzFactory(factory.django.DjangoModelFactory):
    kucharze_dict = {'Jan':15,'Paweł':16,'Krystian':17,'Andrzej':20,
                    "Stasiu":45,'Dąbromir':76}
    
    name = factory.fuzzy.FuzzyChoice(kucharze_dict.keys())
    age = kucharze_dict[name]

    class Meta:
        model=Kucharz
        exclude = ('kucharze_dict',)