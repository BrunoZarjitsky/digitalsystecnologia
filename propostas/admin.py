from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Proposta


@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    # Torna o objeto não editavel quando aprovado ou negado
    def get_readonly_fields(self, request: HttpRequest, obj=None):
        if obj and obj.status != Proposta.StatusPossiveis.EM_ANALISE:
            return [
                'nome_completo',
                'cpf',
                'endereco',
                'valor_emprestimo',
                'status',
            ]
        return ['status']
