from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy
# from  flask_migrate import Migrate, MigrateCommand


app =  Flask(__name__)
bootstrap = Bootstrap(app)
# db = SQLAlchemy()
def create_app():
    app.config.from_object(Config)
    
    
    # db.init_app(app)
    # migrate = Migrate(app, db)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    
    return app
    