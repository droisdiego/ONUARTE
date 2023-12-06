from typing import Self
from django.db import models

# Create your models here.

class PerfilUsuario(models.Model):
    nome = models.CharField(max_length=100)
    pseudonimo = models.CharField(max_length=50)
    icone_perfil = models.ImageField(blank=True, null=True)
    descricao = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Comunidade(models.Model):
    nome_comunidade = models.CharField(max_length=100)
    icone_comunidade = models.ImageField(blank=True, null=True)
    banner = models.ImageField(blank=True, null=True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome_comunidade
    

class Publicacao(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    texto = models.TextField(blank=True, null=True, default='-')
    imagem = models.ImageField(blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.username} - {self.data_publicacao}"
