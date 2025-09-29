import os
from supabase import create_client

def get_supabase_client():
    supabase_url = os.environ.get('SUPABASE_URL')
    supabase_key = os.environ.get('SUPABASE_KEY')
    
    if not supabase_url or not supabase_key:
        raise ValueError("Variáveis SUPABASE_URL e SUPABASE_KEY não configuradas")
    
    return create_client(supabase_url, supabase_key)