from clothes.models import *

from django.test import TestCase


class DateTestCase(TestCase):
  fixtures = ['date_model_testdata.json']
  
  def setUp(self):
    super(DateTestCase, self).setUp()
    self.date1 = Date.objects.get(pk=1)
    self.date2 = Date.objects.get(pk=2)
  
  def test_articles_bought_before_worn(self):
    self.assertFalse(self.date1.articles_bought_before_worn())
    self.assertTrue(self.date2.articles_bought_before_worn())

