
from flask import Flask
from flask import abort
from flask import render_template
from flask import Blueprint
from api import api
from models import db
from models import Bot
from models import Command


ui = Blueprint('ui',  __name__, static_folder='static', static_url_path='/static/webui', template_folder='templates')

@ui.route('/')
def index():
	return render_template('index.html')


@ui.route('/bots')
def bot_list():
	bots = Bot.query.order_by(Bot.id.desc())
	return render_template('bot_list.html', bots=bots)

@ui.route('/bots/<bot_id>')
def bot_detail(bot_id):
	bot = db.session.query(Bot).get(bot_id)
	if not bot:
		abort(404)
	return render_template('bot_detail.html', bot=bot)
