# -*- coding: utf-8 -*-

import socket
from flask import Blueprint


frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    host_name = socket.gethostname()

    return {
        'hostname': host_name,
        'ip': socket.gethostbyname(host_name),
        'status': 'Application up and running!!!'
    }
