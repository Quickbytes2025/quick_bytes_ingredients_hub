from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from App.models.i_user import I_user

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    ingredients = db.relationship('Ingredients', secondary='i_user', backref=db.backref('user', lazy= 'dynamic'),lazy='dynamic')
    recipes = db.relationship('Recipe', secondary='r_user', backref=db.backref('user', lazy= True))

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

