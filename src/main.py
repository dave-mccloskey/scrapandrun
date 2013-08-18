import django.core.handlers.wsgi
import os
import sys

# Include current directory in path
pwd = os.path.abspath(os.path.dirname(__file__))
lib_dir = os.path.join(pwd, 'lib')
sys.path.extend([pwd, lib_dir])

# Define app
app = django.core.handlers.wsgi.WSGIHandler()
