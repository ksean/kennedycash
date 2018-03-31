from datetime import datetime
from django.test import TestCase
from kennedycash.models import *
from djmoney.money import Money


class PersonalTransactionTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Run once before all tests
        Category.objects.create(name='foo')
        category = Category.objects.get(id=1)
        PersonalTransaction.objects.create(date=datetime.now().date(),
                                           description='a description here',
                                           amount=Money(10, 'CAD'))
        personalTransaction = PersonalTransaction.objects.get(id=1)
        personalTransaction.categories.add(category)


    def test_description_content(self):
        personalTransaction = PersonalTransaction.objects.get(id=1)
        expected_object_name = '%s' % (personalTransaction.description,)
        self.assertEquals(expected_object_name, 'a description here')
