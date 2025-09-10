from django import forms
from .models import Card, NFCTag

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'content']

class NFCTagForm(forms.ModelForm):
    class Meta:
        model = NFCTag
        fields = [ 'title', 'card']
