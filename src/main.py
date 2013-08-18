import django.core.handlers.wsgi
import os
import sys

# Include current directory in path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Define app
app = django.core.handlers.wsgi.WSGIHandler()
