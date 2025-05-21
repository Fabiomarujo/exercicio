from django.shortcuts import HttpResponse

# Create your views here.
def instrutor(request): 
    return HttpResponse("Ola! Eu sou o seu Instrutor.")