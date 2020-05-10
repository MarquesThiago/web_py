from django.shortcuts import render

# importando o modulo responsavel pelas respostas http

from django.http import HttpResponse


# todas as aplicações de resposta serão criadas como funções, assim como abaixo

def index(request):
    return HttpResponse("<h1>primeira view</h1>")








# Create your views here.
