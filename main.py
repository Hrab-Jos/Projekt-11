# načtení potřebných modulů a funkcí
from flask import Blueprint, abort, redirect, jsonify, url_for, render_template, make_response
from flask_login import login_required, current_user
from . import db
from .forms import NotifikaceForm
from .models import Notification, User
from sqlalchemy import desc
from pprint import pprint
import json

main = Blueprint('main', __name__)
  

@main.route('/profile')
@login_required
def profile():
	notifications = Notification.query.order_by(Notification.time.desc()).all()
	return render_template('profile.html', name=current_user.username, notifications=notifications)    

@main.route('/notification/<id>')
@login_required
def notification_data(id):
	notification = Notification.query.get(id)
	if notification is None:
		abort(404)

	usernames = list(map(lambda x: x.username, notification.seenUsers.all()))
	return jsonify({ 'users': usernames, 'id': notification.id, 'header': notification.header, 'message': notification.message, 'date': notification.time })
    

@main.route('/notification/<id>/mark-user-seen/<userid>', methods=['POST'])
@login_required
def notification_seen_post(id, userid):
	notification = Notification.query.get(id)
	if notification is None:
		abort(400)

	user = User.query.get(userid)
	if user is None:
		abort(400)


	pprint(user)
	if notification.seenUsers.filter(User.id == userid).first() is None:
		notification.seenUsers.append(user)
		db.session.add(notification)
		db.session.commit()
		return jsonify(success=True)

	return jsonify(success=False)
    

@main.route('/notifikace', methods=['GET','POST'])
@login_required
def notifikace():
	form=NotifikaceForm()
	if form.validate_on_submit():
		# create a new user with the form data. Hash the password so the plaintext version isn't saved.
		new_notification = Notification(header=form.header.data, message=form.message.data)

		# add the new user to the database
		db.session.add(new_notification)
		db.session.commit()

		return redirect(url_for('main.profile'))

	return render_template('notifikace.html', form=form)  


@main.route('/') # při zadání adresy lokálního serveru a znaku / se spustí funkce index a vykreslí stránku index.html, 
def index():
	return render_template('index.html') # při vykreslení předáváme parametr datum, díky kterému na dané stránce proběhne funkce tam kde předáme parametr do dvojitých složených závorek
    
