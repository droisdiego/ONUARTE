from django.contrib import admin
from .models import *


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pseudonimo', 'icone_perfil', 'email')

@admin.register(Comunidade)
class ComunidadeAdmin(admin.ModelAdmin):
    list_display = ('nome_comunidade', 'icone_comunidade', 'banner', 'descricao')

@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ('autor', 'texto', 'imagem', 'data_publicacao')
    list_filter = ('autor', 'data_publicacao')
    search_fields = ('comunidade__nome_comunidade', 'autor__username', 'texto')
