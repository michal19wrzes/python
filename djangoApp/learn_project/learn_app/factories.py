import factory
import factory.django
import factory.fuzzy

from .models import Potrawa,Kucharz

class KucharzFactory(factory.django.DjangoModelFactory):
    kucharze_dict = {'Jan':15,'Paweł':16,'Krystian':17,'Andrzej':20,
                    "Stasiu":45,'Dąbromir':76}
    
    name = factory.fuzzy.FuzzyChoice(kucharze_dict.keys())
    age = kucharze_dict[name.fuzz()]

    class Meta:
        model=Kucharz
        exclude = ('kucharze_dict',)

class PotrawaFactory(factory.django.DjangoModelFactory):
    potrawy_dict = {
                    'name':['ZupaTestowa','Kotlet Anety','Barszcz Ukrainski'],
                    'smak':['dobry','bardzo dobry', 'taki se']
                    }
    
    name = factory.fuzzy.FuzzyChoice(potrawy_dict['name'])
    smak = factory.fuzzy.FuzzyChoice(potrawy_dict['smak'])
    powi = factory.SubFactory(KucharzFactory)

    class Meta:
        model=Potrawa
        exclude = ('potrawy_dict',)