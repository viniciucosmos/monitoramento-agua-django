import os
from supabase import create_client
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import LeiturasSerializer

# Função helper para Supabase
def get_supabase():
    """Retorna cliente Supabase"""
    supabase_url = os.environ.get('SUPABASE_URL')
    supabase_key = os.environ.get('SUPABASE_KEY')
    
    if not supabase_url or not supabase_key:
        raise ValueError("Variáveis SUPABASE_URL e SUPABASE_KEY não configuradas")
    
    return create_client(supabase_url, supabase_key)

# ENDPOINTS ATUALIZADOS
@api_view(['GET'])
def ultima_leitura(request):
    try:
        supabase = get_supabase()
        
        response = supabase.table('monitoramento_leituras') \
                         .select('*') \
                         .order('id', desc=True) \
                         .limit(1) \
                         .execute()
        
        if not response.data:
            return Response({"message": "Nenhuma leitura registrada ainda."}, status=404)
        
        # Usar serializer para formatação
        serializer = LeiturasSerializer(data=response.data[0])
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=500)
        
    except Exception as e:
        return Response({"error": f"Erro ao acessar Supabase: {str(e)}"}, status=500)

@api_view(['POST'])
def registrar_leitura(request):
    try:
        # Validar dados com serializer primeiro
        serializer = LeiturasSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        supabase = get_supabase()
        
        # Inserir no Supabase
        response = supabase.table('monitoramento_leituras') \
                         .insert(serializer.validated_data) \
                         .execute()
        
        if response.data:
            return Response(response.data[0], status=201)
        else:
            return Response({"error": "Falha ao registrar leitura"}, status=400)
            
    except Exception as e:
        return Response({"error": f"Erro ao registrar no Supabase: {str(e)}"}, status=500)

# Views de templates (mantidas iguais)
def dashboard(request):
    return render(request, 'dashboard.html')

def duvidas(request):
    return render(request, 'duvidas.html')