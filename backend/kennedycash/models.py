from django.db import models
from djmoney.models.fields import MoneyField


class Category(models.Model):
    name = models.CharField(max_length=100)
    rule = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Account(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class PersonalTransaction(models.Model):
    date = models.DateField()
    description = models.TextField()
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='CAD')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        category = str(self.category) if self.category is not None else 'Uncategorized'
        return "%s | %s [%s] | %s" % (self.date, self.description, self.amount, category)

    class Meta:
        ordering = ('date', 'description', 'amount',)


class Query(models.Model):
    name = models.CharField(max_length=100)
    rule = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
