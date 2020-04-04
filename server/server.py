from flask import Flask
from flask_script import Manager, Server
from api import api
from ui import ui
from models import db 
from models import Bot
from models import Command
from config import config


app = Flask(__name__)								#New flask obj
app.config.from_object(config['dev'])				#get from config
app.register_blueprint(ui)							#add the blueprint for webserver	
app.register_blueprint(api , url_prefix="/api")		#add the blueprint for api at /api
db.init_app(app)									#init app and manager
manager = Manager(app)
manager.add_command("runserver", Server(host="192.168.1.122", port='80'))

#python server.py initdb 
#initializes database
@manager.command
def initdb():
	db.drop_all()
	db.create_all()
	db.session.commit()

if __name__ == "__main__":
	manager.run()
