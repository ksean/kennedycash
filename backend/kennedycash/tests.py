from django.test import TestCase
from .models import PersonalTransaction


class PersonalTransactionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        PersonalTransaction.objects.create(description='a description here')

    def test_description_content(self):
        personalTransaction = PersonalTransaction.objects.get(id=2)
        expected_object_name = f'{personalTransaction.description}'
        self.assertEquals(expected_object_name, 'a description here')
