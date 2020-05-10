from django.db import models


class Habilidade(models.Model):

    id = models.IntegerField(auto_created=True, null=False, primary_key= True)
    nome = models.CharField(null=False, max_length=150)

    def __str__(self):
        return f"id: {self.id},, nome: {self.nome}"