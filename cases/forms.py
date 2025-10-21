from django import forms
from .models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['first_name', 'last_name', 'country', 'account_number', 'description', 'status']
