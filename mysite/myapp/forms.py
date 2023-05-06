from django import forms
from .models import *


class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['titre', 'description', 'tag']



class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['nom', 'prenom', 'email', 'password']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'email': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control mb-2'}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['libelle']

        widgets = {
            'libelle': forms.TextInput(attrs={'class': 'form-control mb-2'}),

        }


"""class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['valeur']

        widgets = {
            'valeur': forms.NumberInput(attrs={'class': 'form-control mb-2'}),

        }"""


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['url']

        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control mb-2'}),

        }


"""class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']

        widgets = {
            'contenu': forms.TextInput(attrs={'class': 'form-control mb-2'}),

        }"""

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

