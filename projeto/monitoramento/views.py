from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Leituras
from .serializers import LeiturasSerializer

#ENDPOINT

@api_view(['GET'])
def ultima_leitura(request):
    leitura = Leituras.objects.last()
    if leitura is None:
        return Response({"message": "Nenhuma leitura registrada ainda."}, status=404)
    
    serializer = LeiturasSerializer(leitura)
    return Response(serializer.data)

#rota de registro de leituras
@api_view(['POST'])
def registrar_leitura(request):
    serializer = LeiturasSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
