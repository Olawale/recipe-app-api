from django.test import TestCase

from calc import add


class CalcTests(TestCase):

    def test_add_numbers(self):
        self.assertEqual(add(1, 2), 3)