"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

import re

from datetime import datetime
from flask import request
from flask_restx import Resource

from .security import require_auth
from . import api_rest

from simpleeval import simple_eval, SimpleEval
from .MathTool import MathTool as mt

class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]


@api_rest.route('/resource/<string:resource_id>')
class ResourceOne(Resource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}

    def post(self, resource_id):
        json_payload = request.json
        return {'timestamp': json_payload}, 201


@api_rest.route('/secure-resource/<string:resource_id>')
class SecureResourceOne(SecureResource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}


@api_rest.route('/evaluate/<string:mode>/<string:expression>')
class evaluate(Resource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, mode, expression):
        # replace divide with /
        expression = re.sub(r'divide', '/', expression)
        # implicit *
        expression = re.sub(r'(\d)(([(a-zA-Z])|(π)|(e))', r'\1*\2', expression)
        s = mt.getInstance()
        s.angleMode = mode
        return round(s.se.eval(expression), s.precision)
