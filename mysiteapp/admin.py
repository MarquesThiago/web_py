from django.contrib import admin


#importamos os models para os arquivos 
from .model import Departamento
from .model import habilidade
from .model import funcionario

# agora definimos que a atualização e vissualizaçã odos mesmo e uma tarefa adminstrativa
admin.site.register(Departamento.Departamento)
admin.site.register(habilidade.Habilidade)
admin.site.register(funcionario.Funcionario)




# Register your models here.
