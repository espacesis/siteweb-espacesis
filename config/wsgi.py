"""
WSGI config for espacesis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

from django.conf import settings
from django.core.wsgi import get_wsgi_application

#this allows easy placement of apps within the interior
#habaritech directory
project_path = Path(__file__).resolve().parent.parent
sys.path.append(os.path.join(project_path,"espacesi"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

application = get_wsgi_application()
