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

# my_functions = simpleeval.DEFAULT_FUNCTIONS.copy()

@api_rest.route('/evaluate/<string:calculation>')
class evaluate(Resource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, calculation):
        # replace divide with /
        calculation = re.sub(r'divide', '/', calculation)
        # implicit * 
        calculation = re.sub(r'(\d)(([(a-zA-Z])|(π)|(e))', r'\1*\2', calculation)
        s = mt.getInstance()
        return round(s.se.eval(calculation),s.precision)

@api_rest.route('/angleMode/<string:mode>')
class changeAngleMode(Resource):
    """ Unsecure Resource Class: Inherit from Resource """

    def post(self, mode):
        mt.getInstance().angleMode = mode

@api_rest.route('/getAngleMode')
class getAngleMode(Resource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self):
        return mt.getInstance().angleMode