from flask import Flask

app = Flask(__name__)

from pyreceipt.web.routes import web
from pyreceipt.api.routes import api

app.register_blueprint(web)
app.register_blueprint(api)
