from flask_login import UserMixin
from . import db
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from datetime import datetime

Base = declarative_base()

association_table = db.Table('seen_notifications', Base.metadata,
    db.Column('userid', db.ForeignKey('users.id')),
    db.Column('notificationid', db.ForeignKey('notifications.id'))
)

class User(Base, UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    password = db.Column(db.String(100))
    username = db.Column(db.String(1000))


class Notification(Base, UserMixin, db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    header = db.Column(db.String(100))
    message = db.Column(db.String(1000))
    time = db.Column('date_at', db.TIMESTAMP(), default=func.now())
    seenUsers=db.relationship('User', secondary=association_table, lazy="dynamic")

