from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'tag_titulo', 'autor', 'contenido')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'tag_titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo','autor','tag_titulo', 'contenido')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'tag_titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control'})

        }