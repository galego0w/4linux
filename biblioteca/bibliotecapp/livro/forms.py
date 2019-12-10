from django import forms
from .models import Livro

class LivroCreate(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'
