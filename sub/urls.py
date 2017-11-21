"""sub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from loja.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'eleitor', EleitorViewSet, base_name='eleitor')
router.register(r'eleitor', VagaViewSet, base_name='Vaga')
router.register(r'candidato', CandidatoViewSet, base_name='candidato')
router.register(r'voto', VotoViewSet, base_name='voto')
router.register(r'resultado', ResultadoViewSet, base_name='resultado')
router.register(r'usuarios', UserViewSet)
router.register(r'Eleitores', EleitorViewSet)
router.register(r'Vaga', VagaViewSet)
router.register(r'candidato', CandidatoViewSet)
router.register(r'Voto', VotoViewSet)
router.register(r'Resultado', ResultadoViewSet)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
