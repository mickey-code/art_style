from flask_script import Manager , Server
# from app.models import User
from app import create_app
# from  flask_migrate import Migrate, MigrateCommand
# from flask_sqlalchemy import SQLAlchemy


app=create_app()

manager =  Manager(app)
# manager.add_command('db',MigrateCommand)
manager.add_command('runserver',Server(use_debugger=True))
# @manager.shell
# def make_shell_context():
#     return dict(app = app,db = db,User = User )
if __name__=="__main__":
    manager.run()