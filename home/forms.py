from django import forms
from .models import *


# ------------------------------------------------

# Comunidade
class ComunidadeForm(forms.ModelForm):
    class Meta:
        model = Comunidade
        fields = ['nome_comunidade', 'icone_comunidade', 'banner', 'descricao']


# ------------------------------------------------

# Publicações
class PublicacaoForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ['autor', 'texto', 'imagem',]
