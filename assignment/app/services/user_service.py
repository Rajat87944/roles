from app import db
from app.models import User
from app.schemas import user_schema

def create_user(data):
    new_user = User(
        username=data['username'],
        email=data['email'],
        password_hash=data['password_hash']
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def update_user(id, data):
    user = User.query.get_or_404(id)
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.password_hash = data.get('password_hash', user.password_hash)
    db.session.commit()
    return user

def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
