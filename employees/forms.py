

# employees/forms.py
from django import forms
from .models import Employee

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('both', 'Both'),
]

class EmployeeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'textfield'}))

    class Meta:
        model = Employee
        fields = ['employee_id', 'name', 'gender', 'email', 'department', 'address']
        widgets = {
            'employee_id': forms.TextInput(attrs={'class': 'textfield', 'placeholder': 'Employee ID'}),
            'name': forms.TextInput(attrs={'class': 'textfield', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'textfield', 'placeholder': 'Email'}),
            'department': forms.TextInput(attrs={'class': 'textfield', 'placeholder': 'Department'}),
            'address': forms.Textarea(attrs={'class': 'textfield', 'placeholder': 'Address'}),
        }
# employees/forms.py
from django import forms

class SearchForm(forms.Form):
    employee_id = forms.CharField(label='Employee ID', max_length=10, widget=forms.TextInput(attrs={'class': 'textfield', 'placeholder': 'Enter Employee ID'}))
