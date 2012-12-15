import os
import sys

paths = ['/home/dave/clothes.akwire.net', '/home/dave/clothes.akwire.net/dsite']
for path in paths:
  if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'dsite.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

import dsite.monitor
dsite.monitor.start(interval=1.0)

