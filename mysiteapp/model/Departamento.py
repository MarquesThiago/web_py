from django.db import models

class Departamento(models.Model):

    id = models.IntegerField(auto_created= True, null= False, primary_key= True)
    nome = models.CharField(max_length= 100, null= False)
    telefone = models.CharField(max_length=13, null= True)