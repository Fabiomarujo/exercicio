from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request): 
    return HttpResponse("Ola! Eu sou index.")

def exibe_mensagem(request):
    t_html = "<DOCType html><html><body>Ola Mundo</body></html>"
    return HttpResponse(t_html)

def test_render(request):
    return render(request, 'escola.html')
