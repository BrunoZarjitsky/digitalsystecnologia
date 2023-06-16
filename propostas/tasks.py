from settings.celery import app
from .models import Proposta


@app.task
def avalia_proposta(proposta_id):
    todas_propostas = Proposta.objects.all()
    total_aprovadas = todas_propostas.filter(
        status=Proposta.StatusPossiveis.APROVADA).count()
    total_negadas = todas_propostas.filter(
        status=Proposta.StatusPossiveis.NEGADA).count()

    proposta = Proposta.objects.get(id=proposta_id)
    proposta.status = Proposta.StatusPossiveis.APROVADA
    if total_aprovadas > total_negadas:
        proposta.status = Proposta.StatusPossiveis.NEGADA
    proposta.save(update_fields=['status'])
