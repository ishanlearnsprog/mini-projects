from flask import Flask
from routes.employee import employee

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.register_blueprint(employee, url_prefix="/")
    return app
