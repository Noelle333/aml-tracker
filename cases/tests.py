from django.test import TestCase
from .models import Case

class CaseModelTest(TestCase):
    def test_case_creation(self):
        case = Case.objects.create(first_name='Test', last_name='User', country='Polska', account_number='123')
        self.assertEqual(case.first_name, 'Test')
        self.assertEqual(case.status, 'open')

