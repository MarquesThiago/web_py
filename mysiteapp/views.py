from django.shortcuts import render
from django.views.generic import ListView, DetailView

# importando o modulo responsavel pelas respostas http

from django.http import HttpResponse

# importanod o modeilo de departamento dos models 
from .model.Departamento import Departamento
from .model.funcionario import Funcionario


def index(request):
    return render(request, 'index.html')
    

def filter(request, pk):
    out = {}
    out["Funcionarios"] = Funcionario.objects.filter(id_dept = pk)
    print(out["Funcionarios"])
    out["Depth"] = Departamento.objects.get(id = pk)
    return render(request, "filter_depth.html", context= out)


    

class ListDeph(ListView):
    model = Departamento
    template_name = "departamento.html"
    queryset = Departamento.objects.order_by("nome")
    context_object_name = "lista_de_depth"

    def get_context_data(self, **kwargs):
        context = super(ListDeph, self).get_context_data(**kwargs)
        context["Departamento"] = "Lista de Departamento"
        return  context

def new_depth(request):
    return render(request, "new_depth.html")


def new_funcionary(request):
    return HttpResponse(request)


# todas as aplicações de resposta serão criadas como funções, assim como abaixo

# def index(request):

#     deph = Departamento.objects.order_by("id")
#     output = ", ".join([dp.nome for dp in deph])
#     return HttpResponse(output)


# def filter(request, id_deph):

#     deph = Departamento.objects.get(id = id_deph)
#     return HttpResponse(str(deph))


    


# # esta funçã é feita para retornar um objeto com todos os dados de departamento ao nosso template
# def list(request):
    
#     # recebemos os dados e passamos ordenoados pr nome 

#     deph = Departamento.objects.order_by("nome")

#     # passamos um dicionario como saida

#     out = {"depth" : deph, "pagine" : "Departamentos -Lista"}

#     # E retornamos um resposta ao template (template_name) com o conteudo (context) proprimente dito 
#     return render(request, template_name='departamento.html', context=out)








# Create your views here.
