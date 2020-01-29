# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify


core = Blueprint('core', __name__, url_prefix='/')


@core.route('/health/', methods=['GET'])
def health(**kwargs):
    return jsonify({
        'application': {
            "status": "ok"
        }
    })
