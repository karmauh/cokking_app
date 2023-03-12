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
        

class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = CookBook
        fields = ('author', 'title', 'description',  'snippet')
        
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 20}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }