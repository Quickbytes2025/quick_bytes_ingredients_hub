from App.database import db

class Ingredients(db.Model):
    ingredient_id=  db.Column(db.String(5), nullable=False, primary_key= True)
    ingredient_name=  db.Column(db.String(80), nullable=False)

    def __init__(self,ingredient_id,ingredient_name):
        self.ingredient_id=ingredient_id
        self.ingredient_name=ingredient_name
    
