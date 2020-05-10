from django.shortcuts import render

# importando o modulo responsavel pelas respostas http

from django.http import HttpResponse

# importanod o modeilo de departamento dos models 
from .model.Departamento import Departamento


# todas as aplicações de resposta serão criadas como funções, assim como abaixo

def index(request):

    deph = Departamento.objects.order_by("id")
    output = ", ".join([dp.nome for dp in deph])
    return HttpResponse(output)


def filter(request, id_deph):

    deph = Departamento.objects.get(id = id_deph)
    return HttpResponse(str(deph))


# esta funçã é feita para retornar um objeto com todos os dados de departamento ao nosso template
def list(request):
    
    # recebemos os dados e passamos ordenoados pr nome 

    deph = Departamento.objects.order_by("nome")

    # passamos um dicionario como saida

    out = {"depth" : deph}

    # E retornamos um resposta ao template (template_name) com o conteudo (context) proprimente dito 
    return render(request, template_name='departamento.html', context=out)








# Create your views here.
