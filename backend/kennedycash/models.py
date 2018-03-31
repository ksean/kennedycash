from django.db import models
from djmoney.models.fields import MoneyField


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class PersonalTransaction(models.Model):
    date = models.DateField()
    description = models.TextField()
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='CAD')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return "%s | %s [%s] | %s" % (self.date, self.description, self.amount, self.categories)

    class Meta:
        ordering = ('date','description','amount',)