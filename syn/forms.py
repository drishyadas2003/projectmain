from django import forms
from .models import *

class Course_form(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'
        
        
        

class Enquiry_form(forms.ModelForm):
    class Meta:
        model=Enquiry
        fields='__all__'
        
        
        
        
class Carrers_form(forms.ModelForm):
    class Meta:
        model=Carrers
        fields='__all__'
        
        
    
class Carrerapply_form(forms.ModelForm):
    class Meta:
        model=Carrerapply
        fields='__all__'



class Success_form(forms.ModelForm):
    class Meta:
        model=Success
        fields='__all__'