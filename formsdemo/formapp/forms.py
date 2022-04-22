from django import forms

class employeeInfoForm(forms.Form):
    name=forms.CharField()
    salary=forms.IntegerField()