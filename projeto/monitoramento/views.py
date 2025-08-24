from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Leituras
from .serializers import LeiturasSerializer

@api_view(['GET'])
def ultima_leitura(request):
    leitura = Leituras.objects.last()
    serializer = LeiturasSerializer(leitura)
    return Response(serializer.data)



