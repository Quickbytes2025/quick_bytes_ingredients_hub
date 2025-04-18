from App.models import Ingredients
from App.database import db


def create_ingredient(ingredient_id,ingredient_name):
    new_ingredient = Ingredients(ingredient_id=ingredient_id, ingredient_name=ingredient_name)
    db.session.add(new_ingredient)
    db.session.commit()
    return new_ingredient

def get_ingredient_by_username(ingredient_name):
    return Ingredients.query.filter_by(ingredient_name).first()

def get_ingredient(ingredient_id):
    return Ingredients.query.get(ingredient_id)

def get_all_ingredients():
    return Ingredients.query.all()