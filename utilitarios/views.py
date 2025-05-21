from django.shortcuts import HttpResponse

# Create your views here.
def utilitarios(request): 
    return HttpResponse("Ola! Qual o utilitário que você mais usa.")