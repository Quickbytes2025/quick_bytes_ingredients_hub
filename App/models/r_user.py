from App.database import db

class R_user(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id= db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'), nullable=False)