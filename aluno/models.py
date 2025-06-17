from django.db import models
from django.utils import timezone
# Create your models here.
class aluno(models.Model):
    matricula = models.AutoField(primary_key=True, help_text='Matricula do Aluno')
    nome = models.CharField(max_length=70, help_text='Informe o nome do Aluno')
    datainicial = models.DateField(null=False, default=timezone.now(), help_text='Informe a data inicial da matricula')
    datafinal = models.DateField(null=True, blank=True, default=timezone.now(), help_text='Informe a data final') 
  
    def __str__(self):
        return f'{self.matricula} - {self.nome} - {self.datainicial} - {self.datafinal}'