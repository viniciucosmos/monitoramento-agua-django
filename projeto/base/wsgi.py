import os
from django.core.wsgi import get_wsgi_application
import sys

sys.path.append('/app/projeto')
sys.path.append('/app')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.base.settings')
application = get_wsgi_application()
