from django.shortcuts import render
from django.views.generic import ListView, DetailView

# importando o modulo responsavel pelas respostas http

from django.http import HttpResponse

# importanod o modeilo de departamento dos models 
from .model.Departamento import Departamento


# todas as aplicações de resposta serão criadas como funções, assim como abaixo

def index(request):

    deph = Departamento.objects.order_by("id")
    output = ", ".join([dp.nome for dp in deph])
    return HttpResponse(output)


# def filter(request, id_deph):

#     deph = Departamento.objects.get(id = id_deph)
#     return HttpResponse(str(deph))


class Filter(DetailView):
    model = Departamento
    template_name = 'filter_depth.html'
    


# # esta funçã é feita para retornar um objeto com todos os dados de departamento ao nosso template
# def list(request):
    
#     # recebemos os dados e passamos ordenoados pr nome 

#     deph = Departamento.objects.order_by("nome")

#     # passamos um dicionario como saida

#     out = {"depth" : deph, "pagine" : "Departamentos -Lista"}

#     # E retornamos um resposta ao template (template_name) com o conteudo (context) proprimente dito 
#     return render(request, template_name='departamento.html', context=out)


class ListDeph(ListView):
    model = Departamento
    template_name = "departamento.html"
    queryset = Departamento.objects.order_by("nome")
    context_object_name = "lista_de_depth"

    def get_context_data(self, **kwargs):
        context = super(ListDeph, self).get_context_data(**kwargs)
        context["Departamento"] = "Lista de Departamento"
        return  context







# Create your views here.
