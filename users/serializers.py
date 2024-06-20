from rest_framework import serializers
from .models import Gerente

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gerente
        fields = ['id', 'nome_completo', 'cpf', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = Gerente.objects.create_user(
            nome_completo=validated_data['nome_completo'],
            cpf=validated_data['cpf'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
