# Generated by Django 3.2.16 on 2023-06-15 17:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=256, verbose_name='Nome Completo')),
                ('cpf', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('[0-9]{11}')], verbose_name='CPF')),
                ('endereco', models.CharField(max_length=256, verbose_name='Endereço')),
                ('valor_emprestimo', models.FloatField(verbose_name='Valor do empréstimo pretendido')),
                ('status', models.CharField(choices=[('em_analise', 'Em análise'), ('aprovada', 'Aprovada'), ('negada', 'Negada')], default='em_analise', max_length=16, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Proposta',
                'verbose_name_plural': 'Propostas',
            },
        ),
    ]
