from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'isbn', 'genre', 'publication_date']

        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter book title'
            }),
            'author': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter author name'
            }),
            'description': forms.Textarea(attrs={
                'class':'form-control',
                'rows':4,
                'placeholder':'Enter book description'
            }),
            'isbn': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter ISBN'
            }),
            'genre': forms.Select(attrs={
                'class':'form-control',
            }),
            'publication_date': forms.DateInput(attrs={
                'class':'form-control',
                'type': 'date'
            })
        }