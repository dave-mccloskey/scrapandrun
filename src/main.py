import django.core.handlers.wsgi
import os
import sys

# Include current directory in path
pwd = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, pwd)

lib_dir = os.path.join(pwd, 'lib')
sys.path.insert(0, os.path.join(lib_dir, 'gdata-2.0.17/src'))
sys.path.insert(0, os.path.join(lib_dir, 'lib/django-picasa-1.3'))
sys.path.insert(0, os.path.join(lib_dir, 'lib/South-0.7.6'))

# Define app
app = django.core.handlers.wsgi.WSGIHandler()
