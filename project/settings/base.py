# -*- coding: utf-8 -*-

#
# Define here the base configuration..
#

import os


DEBUG = False

# JWT
JWT_LIFESPAN = 60*60*24
JWT_ISSUER = 'flask-app-blueprint'
JWT_ALGORITHM = 'HS256'  # HS256, RS256

# And after that...
# Used to define some configuration in the local environment in order to
# don't modify the repository code...
try:
    from .local import *
except ImportError:
    pass
