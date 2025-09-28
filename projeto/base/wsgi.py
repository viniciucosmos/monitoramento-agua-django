import os
from django.core.wsgi import get_wsgi_application
import sys

# Adicione o path para a pasta projeto
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'projeto'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
application = get_wsgi_application()
