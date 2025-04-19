from App.database import db

class I_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id =  db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    ingredient_id =  db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'), primary_key=True)