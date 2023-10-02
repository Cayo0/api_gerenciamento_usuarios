from rest_framework import serializers
from .models import UsuarioPersonalizado

class UsuarioSerializer(serializers.ModelSerializer):
    """
    classe que vai serializar os dados do modelo de usuario personalizado onde o 
    campo password é apenas para inserir dados, ele não será incluído para leitura 
    nos objetos serializados, o que significa que o campo password não será exposto
    quando os dados forem serializados.
    """
    class Meta:
         model = UsuarioPersonalizado
         fields = ['username', 'email', 'first_name', 'last_name', 'data_de_nascimento', 'password', 'numero_telefone']
         extra_kwargs = {'password': {'write_only': True}}

