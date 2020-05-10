from django.db import models
from .Departamento import Departamento
from .habilidade import Habilidade

class Funcionario(models.Model): 

    id_dept = models.ForeignKey(Departamento, on_delete = models.CASCADE)
    id_habilidades = models.ManyToManyField(Habilidade)
    
    nome = models.CharField(max_length=255)
    nascimento = models.DateField()
    antiguidade = models.IntegerField(default=0)


    def __str__(self):
        return f"nome : {self.nome}, nascimento: {self.nascimento}, antiguidad: {self.antiguidade}"
    
