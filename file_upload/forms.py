from django import forms
from .models import Document

class DateInput(forms.DateInput):
    input_type = 'date'

class DocumentForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Document
        fields = ('title', 'date', 'pdf', 'cover')
        widgets = {'date' : DateInput}