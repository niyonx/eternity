import os
from flask import Flask, current_app, send_file

from .api import api_bp
from .client import client_bp

from flask import jsonify
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
# app = Flask(__name__)
# app.config.from_object(__name__)

app = Flask(__name__, static_folder='../dist/static')
app.register_blueprint(api_bp)
# app.register_blueprint(client_bp)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

from .config import Config
app.logger.info('>>> {}'.format(Config.FLASK_ENV))

@app.route('/')
def index_client():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)


