from flask import Flask
from flask_script import Manager, Server
from api import api
from ui import ui
from models import db 
from models import Bot
from models import Command
from config import config
from flask_bootstrap import Bootstrap

app = Flask(__name__)		
			#New flask obj
app.config.from_object(config['dev'])				#get from config
app.register_blueprint(ui)							#add the blueprint for webserver	
app.register_blueprint(api , url_prefix="/api")		#add the blueprint for api at /api

bootstrap = Bootstrap(app)									#init app and manager
manager = Manager(app)
manager.add_command("runserver", Server(host="10.0.0.14", port='80'))
db.init_app(app)			
#python server.py initdb 
#initializes database
@manager.command
def initdb():
	db.drop_all()
	db.create_all()
	bot = Bot(1234)
	bot.ip = 'asdfas'
	db.session.add(bot)
	db.session.commit()

if __name__ == "__main__":
	manager.run()
