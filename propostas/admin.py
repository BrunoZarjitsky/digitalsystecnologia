from django.contrib import admin
from django.http.request import HttpRequest
from .models import Proposta
from rabbit_utils.rabbit_utils import RabbitService


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

    # Solicita a avaliação do objetos selecionados
    @admin.action(description="Solicitar avaliação")
    def solicitar_avaliacao(self, request, queryset):
        propostas_atualizar = []
        for proposta in queryset:
            if proposta.status != Proposta.StatusPossiveis.EM_ANALISE:
                continue
            propostas_atualizar.append(proposta.id)
        service = RabbitService()
        message = service.create_message(
            task="propostas.tasks.avalia_lista_propostas",
            args=[propostas_atualizar]
        )
        service.publish_message(
            queue='celery',
            message=message
        )
        service.close_connection()

    # Define o status dos objetos selecionados como em analise
    @admin.action(description="Bota em análise")
    def em_analise(self, request, queryset):
        queryset.update(status=Proposta.StatusPossiveis.EM_ANALISE)

    actions = ["solicitar_avaliacao", "em_analise"]
