from django.shortcuts import HttpResponse

def aluno(request):
    t_html = "<!DOCTYPE html><html><body><h1>Nome: Fábio Anderson</h1></body></html>"
    return HttpResponse(t_html)


