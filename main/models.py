from django.db import models

class PessoaF(models.Model):
    nomecomp = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.IntegerField()
    
    def __str__(self):
        return self.nomecomp

class PessoaJ(models.Model):
    empresa = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.IntegerField()
    
    def __str__(self):
        return self.empresa