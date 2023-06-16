from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from rabbit_utils.rabbit_utils import RabbitService


class Proposta(models.Model):
    nome_completo = models.CharField(
        max_length=256,
        verbose_name="Nome Completo"
    )
    cpf = models.CharField(
        max_length=11,
        validators=[RegexValidator('[0-9]{11}')],
        verbose_name="CPF"
    )
    endereco = models.CharField(max_length=256, verbose_name="Endereço")
    valor_emprestimo = models.FloatField(
        verbose_name="Valor do empréstimo pretendido"
    )

    class StatusPossiveis(models.TextChoices):
        EM_ANALISE = "em_analise", _("Em análise"),
        APROVADA = "aprovada", _("Aprovada"),
        NEGADA = "negada", _("Negada"),

    status = models.CharField(
        max_length=16,
        choices=StatusPossiveis.choices,
        default=StatusPossiveis.EM_ANALISE,
        verbose_name="Status"
    )

    class Meta:
        verbose_name = "Proposta"
        verbose_name_plural = "Propostas"

    def __str__(self):
        return f"{self.cpf} - {self.valor_emprestimo}"


@receiver(post_save, sender=Proposta, dispatch_uid="chama_avalia_proposta")
def chama_avalia_proposta(sender, instance, created, **kwargs):
    # if instance.status != Proposta.StatusPossiveis.EM_ANALISE:
    if not created:
        return None
    service = RabbitService()
    message = service.create_message(
        task="propostas.tasks.avalia_proposta",
        args=[instance.id]
    )
    service.publish_message(
        queue='celery',
        message=message
    )
    service.close_connection()
