# Generated by Django 5.2.1 on 2025-06-02 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiposdeatividades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipodeatividade',
            name='descricao',
            field=models.CharField(help_text='Informe a descrição do Tipo de Atividade', max_length=100),
        ),
    ]
