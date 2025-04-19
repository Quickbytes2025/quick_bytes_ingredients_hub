from App.database import db

class R_ingredients(db.Model):
    __tablename__ = 'r_ingredients'
    recpie_id=  db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'), primary_key=True)
    ingredient_id= db.Column(db.Integer,db.ForeignKey('ingredients.ingredient_id'), primary_key=True)
     
    def __init__(self,recipe_id,ingredient_id):
        self.recpie_id=recipe_id
        self.ingredient_id=ingredient_id
