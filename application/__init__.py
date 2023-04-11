from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config.from_object('config_template.Config')

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    from .models import Users, Expenses

    db.init_app(app)

    if not path.exists(app.config['DATABASE_NAME']):
        db.create_all(app=app)
        print('Created Database!')

    return app