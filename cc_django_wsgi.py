# *coding: utf-8*
import sys
import os
 
sys.path.append("/home/bas/app_e7a18983-405e-4ada-ac68-2738f2767461")
os.environ['DJANGO_SETTINGS_MODULE'] = 'cc_django.settings'
os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-egg'
 
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
