from django.db import models
from django.utils import timezone

from tiposdeatividades.models import TipoDeAtividade
from aluno.models import aluno
from instrutor.models import Instrutor

# Create your models here.
class Turma(models.Model):
    numero = models.AutoField(primary_key=True, help_text='Número da Turma')
    horarioAula = models.TimeField(help_text='Horário da Aula')
    duracaoAula = models.SmallIntegerField(help_text='Entre com a duração da Aula')
    dataInicial = models.DateField(null=False, default=timezone.now(), help_text='Informe a data inicial da matricula')
    dataFinal = models.DateField(null=True, blank=True, help_text='Informe a data final')

    codigo_atividade = models.ForeignKey(TipoDeAtividade, null=True, blank=True, on_delete=models.CASCADE, related_name='atividades')
    matricula_monitor = models.ForeignKey(aluno, null=True, blank=True, on_delete=models.SET_NULL, related_name='alunos')
    id_instrutor = models.ForeignKey(Instrutor, null=True, blank=True, on_delete=models.CASCADE, related_name='instrutores')

    def __str__(self):
        return f'{self.numero} - {self.horarioAula} - {self.duracaoAula} - {self.dataInicial} - {self.dataFinal}'