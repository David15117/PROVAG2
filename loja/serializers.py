from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from loja.models import *
class UserSerializer(serializers.HyperlinkedModelSerializer):
    	class Meta:
		model = User
		fields = ('url', 'username', 'email')
	def create(self, validated_data):
		user = User.objects.create(**validated_data)# pega todos objetos de usuario
		return user#Sempre deve retorna
class EleitorSerializer(serializers.HyperlinkedModelSerializer):
    	usuario = UserSerializer(many=False)
	class Meta:
		model = Eleitor
		fields = ('__all__')
	def create(self,dados):
		dados_user=dados.pop('usuario')# remove usuario
		u = User.objects.create(**dados_user)# criar o usuario
		p = Eleitor.objects.create(usuario=u,**dados)#criar pessoa, e em dados insere objetivo de usuario
		return p
class VagaSerializer(serializers.HyperlinkedModelSerializer):
    	class Meta:
		model = Vaga
		fields = '__all__'
	def create(self, dados):
		dados_evento = 	Vaga.objects.create(**dados)
		return dados_evento
class CandidatoSerializer(serializers.HyperlinkedModelSerializer):
    	vaga = VagaSerializer(many=False)
	class Meta:
		model = Candidato
		fields = ('__all__')
	def create(self,dados):
		dados_evento = dados.pop('evento')
		evento = Vaga.objects.get(nome=dados_evento)
		candidato = Candidato.objects.create(evento = evento,**dados)
class VotoSerializer(serializers.HyperlinkedModelSerializer):
    #evento = EventoSerializer(many=False)
    #autor = AutorSerializer(many=False)
    class Meta:
        model = Voto
        fields = ('__all__')
class ResultadoSerializer(serializers.HyperlinkedModelSerializer):
    #evento = EventoSerializer(many=False)
    #autor = AutorSerializer(many=False)
    class Meta:
        model = Resultado
        fields = ('__all__')