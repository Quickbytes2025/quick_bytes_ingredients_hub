from App.models import R_ingredients
from App.models import Ingredients
from App.database import db

def create_r_ingredient(recipe_id, ingredient_name, ingredient_num):
    pull_ingredient = R_ingredients(recipe_id=recipe_id, ingredient_name=ingredient_name, ingredient_num=ingredient_num)
    db.session.add( pull_ingredient)
    db.session.commit()
    return pull_ingredient

def get_ingredients_by_recipe(recipe_id):
    return R_ingredients.query.filter_by(recipe_id=recipe_id).all()

def get_r_ingredient(r_ingredient_name):
    return Ingredients.query.filter_by(ingredient_name=r_ingredient_name).first()

def get_all_ingredients():
    return R_ingredients.query.order_by(R_ingredients.recpie_id).all()