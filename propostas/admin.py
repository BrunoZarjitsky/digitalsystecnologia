from django.contrib import admin
from .models import Proposta


@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    pass
