from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from qp.config import Config

db = SQLAlchemy(app)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    from qp.main.routes import main
    from qp.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(errors)
    return app