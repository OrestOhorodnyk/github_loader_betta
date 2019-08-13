from datetime import datetime
from flask_login import UserMixin
from github_loader import db, login_manager
from sqlalchemy import DateTime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    github_id = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    created_date = db.Column(DateTime, default=datetime.utcnow)

    def __init__(self, github_user):
        self.github_id = github_user['id']
        self.username = github_user['name']
        self.email = github_user['email']
        self.authenticated = True

    def __repr__(self):
        return f"User('{self.username}', '{self.email}'"

