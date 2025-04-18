from App.database import db

class Recipe(db.Model):
    recipe_id= db.Column(db.String(5), primary_key=True)
    recipe_name= db.Column(db.String(120), nullable=False)
    recipe_instructions = db.Column(db.String(2500), nullable=False)
    recipe_thumbnail= db.Column(db.String(120), nullable=False)

    def __init__ (self,recipe_id,recipe_name,recipe_instructions, recipe_thumbnail):
        self.recipe_id=recipe_id
        self.recipe_name=recipe_name
        self.recipe_instructions=recipe_instructions
        self.recipe_thumbnail = recipe_thumbnail