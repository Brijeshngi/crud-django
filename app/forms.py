from django import forms
from .models import todo
from django.utils import timezone
 
class todoform(forms.ModelForm):
    class Meta:
        model = todo
        fields="__all__"


class EditForm(forms.ModelForm):
    class Meta:
        model = todo
        fields ="__all__" 
        