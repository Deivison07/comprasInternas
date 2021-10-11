
from django.forms import ModelForm
from django import forms

# a forma que o framework entrega campos de formulário veinculadas a um banco de dados especifico

class FormularioSimples(forms.Form): # criando um formulario simples sem estar vinculado a um banco de dados
    nome = forms.CharField(label='Nome') # os campos do formulário
    senha = forms.CharField(label='Senha')