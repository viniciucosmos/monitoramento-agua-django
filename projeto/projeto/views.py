from django.http  import HttpResponse

def teste_view(request):
    return HttpResponse("Rota de Teste! ")