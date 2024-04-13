from myapp.models import *
from django import forms
from captcha.fields import CaptchaField


class EmployeeForm(forms.ModelForm):
    captcha= CaptchaField()
    class Meta:
        model = Employee
        fields = ['name','email','captcha']

