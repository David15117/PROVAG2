# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Eleitor(models.Model):
    nome = models.CharField(max_length=128)
    token = models.CharField(max_length=20)
    idade = models.IntegerField()
    tipo = models.BooleanField("Conselho",default=True)
    usuario = models.ForeignKey(User, null=True, blank=False)
    def __str__(self):
        return '{}'.format(self.nome)
class Vaga(models.Model):
    nomedavaga = models.CharField(max_length=128)
    quantidade = models.FloatField()
    def __str__(self):
        return '{}'.format(self.nomedavaga)
class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    vaga = models.ForeignKey(Vaga, related_name = 'vaga_voto', null = True, blank = True)
    sexo = models.CharField(max_length=1)
    idade = models.IntegerField()
    descricao = models.TextField()
    def __str__(self):
        return '{}'.format(self.nome)
class Voto(models.Model):
    eleitor = models.OneToOneField(Eleitor, related_name = 'vota_voto', null = True, blank = True)
    candidato = models.ForeignKey(Candidato, related_name = 'candidato_voto', null = True, blank = True)
    branco = models.BooleanField("Voto Em Branco?",default=True)
    def __str__(self):
        return '{}'.format(self.candidato)
class Resultado(models.Model):
    resultado = models.ForeignKey(Voto, related_name = 'resultado_voto', null = True, blank = False)
    tipo = models.BooleanField("Libera",default=True)
    def __str__(self):
        return '{}'.format(self.resultado)