from App.database import db

class Recipe(db.Model):
    __tablename__ = 'recipe'
    recipe_id= db.Column(db.Integer, primary_key=True)
    recipe_name= db.Column(db.String(120), nullable=False, unique =True)
    recipe_instructions = db.Column(db.String(2500), nullable=False)
    recipe_thumbnail= db.Column(db.String(120), nullable=False)
    ingredients = db.relationship('Ingredients', secondary='r_ingredients', backref=db.backref('recipe', lazy= True))
    category = db.Column(db.String(30),db.ForeignKey('category.category_name'), nullable=False)



    def __init__ (self,recipe_id,recipe_name,recipe_instructions, recipe_thumbnail, category):
        self.recipe_id=recipe_id
        self.recipe_name=recipe_name
        self.recipe_instructions=recipe_instructions
        self.recipe_thumbnail = recipe_thumbnail
        self.category=category