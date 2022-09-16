from django import forms  
from django.core import validators
from employee.models import Employee  
class EmployeeForm(forms.ModelForm):  
    #using Validators in name field
    ename = forms.CharField(validators=[validators.MaxLengthValidator(6)])
    class Meta:  
        model = Employee  
        fields = "__all__"  