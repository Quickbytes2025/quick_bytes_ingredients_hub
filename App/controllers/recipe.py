from App.models import Recipe
from App.database import db

def create_recipe( recipe_id, recipe_name, recipe_thumbnail):
    new_recipe = Recipe(recipe_id=recipe_id,   recipe_name=recipe_name,  recipe_thumbnail=recipe_thumbnail)
    db.session.add(new_recipe)
    db.session.commit()
    return new_recipe

def get_recipe_by_name(recipe_name):
    return Recipe.query.filter_by(recipe_name=recipe_name).first()

def get_recipe(recipe_id):
    return Recipe.query.get(recipe_id)

def get_all_recipes():
    return Recipe.query.all()