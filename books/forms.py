from django import forms
from .models import Book

class BookForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','description','publisher','pubished_date','pages']
    