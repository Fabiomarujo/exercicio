from django import forms

# Class formulário para iniciado

class InstrutorForm(forms.Form):    
    rg = forms.CharField(max_length=15, help_text='Informe o RG do Instrutor')
    nome = forms.CharField(max_length=70, help_text='Informe o nome do Instrutor')
    dataNascimento = forms.CharField(required=True, help_text='Informe a data de Nascimento')
    telefone = forms.CharField(max_length=9, help_text='Informe o número de telefone')
    ddd = forms.CharField(max_length=3, help_text='Informe o DDD')
    # codigoTitulo = forms.CharField(required=True)
    # codigoTitulo = forms.ForeignKey(Titulo, null=True, blank=True, related_name='titulos', on_delete=models.SET_NULL, db_column='titulo_codigo')

class InstrutorAtualizarForm(forms.Form):
    # id = forms.IntegerField(primary_key=True, help_text='Identificacao do Instrutor')
    rg = forms.CharField(max_length=15, help_text='Informe o RG do Instrutor')
    nome = forms.CharField(max_length=70, help_text='Informe o nome do Instrutor')
    dataNascimento = forms.CharField(required=True, help_text='Informe a data de Nascimento')
    telefone = forms.CharField(max_length=9, help_text='Informe o número de telefone')
    ddd = forms.CharField(max_length=3, help_text='Informe o DDD')
    # codigoTitulo = forms.CharField(null=True, blank=True)