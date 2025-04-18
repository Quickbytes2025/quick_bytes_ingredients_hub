from App.database import db

class R_ingredients(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    recpie_id=  db.Column(db.String(5), db.ForeignKey('recipe.recipe_id'), nullable=False)
    ingredient_num=  db.Column(db.String(20), nullable=False)
    ingredient_name= db.Column(db.String(30), nullable=False)
    recipes = db.relationship('Recipe', backref='recipe_ingredients', lazy= True)

    def __init__(self,recipe_id,ingredient_name,ingredient_num):
        self.recpie_id=recipe_id
        self.ingredient_name=ingredient_name
        self.ingredient_id=ingredient_num