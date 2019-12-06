from django import forms
from .models import Estoque, EstoqueItens


class EstoqueForm(forms.ModelForm):

    class Meta:
        model = Estoque
        fields = ('safra',)


class EstoqueItensForm(forms.ModelForm):

    class Meta:
        model = EstoqueItens
        fields = '__all__'
