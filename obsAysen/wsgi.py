"""
WSGI config for obsAysen project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
>>>>>>> 4f49121395f68597e3377a685bf7eca3eb362961
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "obsAysen.settings")

application = get_wsgi_application()
