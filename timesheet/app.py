from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from routes.employee import employee
from models import db, Employee

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///./timesheet.db"
    app.config["JWT_SECRET_KEY"]="SDAKFJASxkkfad"
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    db.init_app(app)
    jwt = JWTManager(app)
    app.register_blueprint(employee, url_prefix="/")
    migrate = Migrate(app, db)
    return app
