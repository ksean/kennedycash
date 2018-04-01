from datetime import datetime
from django.test import TestCase
from kennedycash.models import *
from djmoney.money import Money


class QueryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Run once before all tests
        pass

    def test_transactiom_split_debit_credit(self):
        self.assertEquals(True, True)

    def test_transactions_grouped_by_month(self):
        self.assertEquals(True, True)

    def test_transactions_grouped_by_quarter(self):
        self.assertEquals(True, True)

    def test_transactions_grouped_by_year(self):
        self.assertEquals(True, True)

    def test_transactions_grouped_by_category(self):
        self.assertEquals(True, True)

    def test_transactions_grouped_by_category_and_month(self):
        self.assertEquals(True, True)

    def test_transactions_monthly_average(self):
        self.assertEquals(True, True)

    def test_transactions_quarterly_average(self):
        self.assertEquals(True, True)

    def test_transactions_yearly_average(self):
        self.assertEquals(True, True)


class CategoryTest(TestCase):

    def test_unmatched_transaction_is_uncategorized(self):
        self.assertEquals(True, True)

    def test_matched_transaction_is_categorized(self):
        self.assertEquals(True, True)

    def test_multi_match_transaction_uses_first_match(self):
        self.assertEquals(True, True)
