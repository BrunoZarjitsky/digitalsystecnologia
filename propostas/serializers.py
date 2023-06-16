from rest_framework import serializers
from .models import Proposta


class PropostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposta
        fields = [
            'id',
            'nome_completo',
            'cpf',
            'endereco',
            'valor_emprestimo',
            'status',
        ]
