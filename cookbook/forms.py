from django import forms
from .models import CookBook


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = CookBook
        fields = ('title', 'description', 'snippet')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 20}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }