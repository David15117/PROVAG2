# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from loja.models import *
from django.contrib import admin

# Register your models here.
admin.site.register(Eleitor)
admin.site.register(Vaga)
admin.site.register(Candidato)
admin.site.register(Voto)
admin.site.register(Resultado)