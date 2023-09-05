from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from map import bahia, sergipe
from datetime import datetime 

class Lead(models.Model):
    ops = [('emprestimo', 'Empréstimo'),('consorcio', 'Consórcio'),('conta', 'Conta Corrente'),('outros', 'Outros')]
    lista_cidades = list(zip([i.lower() for i in bahia], bahia)) + list(zip([i.lower() for i in sergipe], sergipe))
    nome= models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    cidade = models.CharField(max_length=100, choices=lista_cidades, default=' ', null=False, blank=False)
    operacao = models.CharField(max_length=30, choices=ops, null=False, blank=False)
    telefone = PhoneNumberField(region='BR')
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    ops = [('emprestimo', 'Empréstimo'),('consorcio', 'Consórcio'),('conta', 'Conta Corrente'),('outros', 'Outros')]
    sexo = [('masculino', 'Masculino'), ('feminino','Feminino')]
    nome_completo = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(default=None, null=False, blank=False)
    sexo = models.CharField(max_length=10, choices=sexo, null=True, blank=True)
    operacao = models.CharField(max_length=30, choices=ops, default=' ', blank=False)
    rg = models.CharField(max_length=10, null=False, blank=False)
    nmr_contrato = models.CharField(max_length=20, null=False, blank=False)
    data_contrato = models.DateTimeField(default=datetime.now, null=False, blank=False)
    duracao_contrato = models.IntegerField(default=0, null=False, blank=False)


    def __str__(self):
        return self.nome_completo