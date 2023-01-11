import bcrypt
from sqlalchemy import event
from .user import User
from .database import db


@event.listens_for(User.__table__, 'after_create')
def create_user(*args, **kwargs):
    db.session.add(
        User(username='smart', password=bcrypt.hashpw('smart'.encode('utf-8'), bcrypt.gensalt(10)),
             email='smarty@hotmail.com',
             bookmark=None, favorite=None))
    db.session.commit()