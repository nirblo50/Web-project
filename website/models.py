from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

MAX_LEN = 100


class User(db.Model, UserMixin):
    """
    This class represents a user in the site
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(MAX_LEN), unique=True)
    password = db.Column(db.String(MAX_LEN))
    first_name = db.Column(db.String(MAX_LEN))
    notifications = db.Column(db.BOOLEAN)
    posts = db.relationship('Post', backref='user', passive_deletes=True)
    favorites = db.relationship('Favorite', backref='user', passive_deletes=True)


class Post(db.Model):
    """
    This class represents a post that users write and save to the DB
    """
    __searchable__ = ['text']

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)


class Favorite(db.Model):
    """
    This class represents a post that a user flagged as favorite
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey(
        'post.id', ondelete="CASCADE"), nullable=False)