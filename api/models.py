# from extensions import db, bcrypt
from uuid import uuid4
from flask_login import  UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()

def generate_uuid():
    return str(uuid4().hex)

# Database models
class User(UserMixin, db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid, unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    hash_password = db.Column(db.String(80), nullable=False)
    
    def set_password(self, password):
        self.hash_password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.hash_password, password)


class Task(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid, unique=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
