from django.db import models
from djmoney.models.fields import MoneyField


class PersonalTransaction(models.Model):
    date = models.DateField()
    description = models.TextField()
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='CAD')