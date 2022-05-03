from django.test import TestCase
from .models import Kucharz,Potrawa
from .factories import KucharzFactory, PotrawaFactory
# Create your tests here.
class KucharzTestCase(TestCase):
    def setUp(self):
        self.kucharze = KucharzFactory.build_batch(3)
        self.potrawy = PotrawaFactory.build_batch(3)

    def test_kucharz_creation(self):
        for kucharz in self.kucharze:
            kucharz.save()
        self.assertIsNotNone(kucharz.id)

    def test_potrawa_creation(self):
        for potrawa in self.potrawy:
            potrawa.powi.save()
            potrawa.save()
            self.assertIsNotNone(potrawa.id)