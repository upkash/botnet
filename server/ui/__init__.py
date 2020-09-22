from flask_login import LoginManager, current_user, login_user
from flask import Flask
from flask import abort
from flask import render_template
from flask import Blueprint
from api import api
from models import db
from models import Bot
from models import Command
# from models import User


ui = Blueprint('ui',  __name__, static_folder='static', static_url_path='/static/webui', template_folder='templates')
# login = LoginManager(ui)

# @ui.route('/login', methods=['GET', 'POST'])
# def login():
# 	if current_user.is_authenticated:
# 		return redirect(url_for('index'))
# 	form = LoginForm()
# 	if form.validate_on_submit():
# 		user = User.query.filter_by(username=form.username.data).first()
# 		if user is None or not user.check_password(form.password.data):
# 			flash("wrong")
# 			return redirect(url_for('login'))
# 		login_user(user, remember = form.remember_me.data)
# 		return redirect(url_for('index'))
# 	return render_template('login.html', title="Login", form=form)

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
	commands = db.session.query(Command).filter(Command.bot == bot)
	if not bot:
		abort(404)
	return render_template('bot_detail.html', bot=bot, commands = commands)
