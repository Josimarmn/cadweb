from django import forms
from .models import *
from datetime import date


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'ordem']
        widgets = {
            'nome':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'ordem':forms.NumberInput(attrs={'class': 'inteiro form-control', 'placeholder': ''}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'datanasc']
        widgets = {
            'nome':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'cpf':forms.TextInput(attrs={'class': 'cpf form-control', 'placeholder': 'C.P.F'}),
            'datanasc': forms.DateInput(attrs={'class': 'data form-control', 'placeholder': 'Data de Nascimento'}, format='%d/%m/%Y'),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if len(nome) < 3:
            raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return nome  
                    
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if len(cpf) < 14:
            raise forms.ValidationError("O campo cpf deve ser conter 11 dígitos.")
        return cpf
    
    def clean_datanasc(self):
        datanasc = self.cleaned_data.get('datanasc')
        if datanasc > date.today():
            raise forms.ValidationError("O campo data deve ser menor que a data atual.")
        return datanasc


