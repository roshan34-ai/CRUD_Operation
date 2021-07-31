from django import forms
from .models import Student

class Student_Form(forms.ModelForm):
    class Meta:
        model=Student
        fields=['id', 'name', 'roll_no', 'email', 'address', 'mob_no']
        widgets={
         'name':forms.TextInput(attrs={'class':'form-control'}),
         'roll_no':forms.TextInput(attrs={'class':'form-control'}),
         'email':forms.EmailInput(attrs={'class':'form-control'}),
         'address':forms.TextInput(attrs={'class':'form-control'}),
         'mob_no':forms.TextInput(attrs={'class':'form-control'}),
        }
