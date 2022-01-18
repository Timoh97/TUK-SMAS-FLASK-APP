from . import db
from datetime import datetime
from . import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    __tablename__ = 'users'
    
    id=db.Column(db.Integer, primary_key=True)
    username=db.column(db.String(255))
    email = db.Column(db.String(200),unique = True,index = True)
    bio = db.Column(db.String(200))
    profile_pic_path = db.Column(db.String)
    password_hash = db.Column(db.String(200))
    
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    
    def __repr__(self):
        return f'User {self.username}'
    
class Post(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200))
    content = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    time_created = db.Column(db.DateTime(timezone = True), default = datetime.now)
    
    def save_post(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_posts(cls):
        posts = Post.query.all()
        return posts

class Subscriber(db.Model):
    id=db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(200),unique = True,index = True)
    
    def save_subscribers(self):
      db.session.add(self)
      db.session.commit()
      
    def __repr__(self):
        return f'Subscriber{self.email}'