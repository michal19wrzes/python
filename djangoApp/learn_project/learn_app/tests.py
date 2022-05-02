from django.test import TestCase
from .models import Kucharz,Potrawa
from .factories import KucharzFactory
# Create your tests here.
class KucharzTestCase(TestCase):
    def setUp(self):
        self.kucharze = KucharzFactory.build_batch(3)
        

    def test_czy_michal_programista(self):
        self.assertTrue(False,'Michal jest programista')