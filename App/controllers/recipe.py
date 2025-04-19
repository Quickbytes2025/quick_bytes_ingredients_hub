from App.models import Recipe
from App.models import Ingredients
from App.database import db

def create_recipe( recipe_id, recipe_name,  recipe_instructions, recipe_thumbnail, category):
    new_recipe = Recipe(recipe_id=recipe_id,   recipe_name=recipe_name, recipe_instructions= recipe_instructions,  recipe_thumbnail=recipe_thumbnail, category=category)
    db.session.add(new_recipe)
    db.session.commit()
    return new_recipe

def get_recipe_by_name(recipe_name):
    search_recipe= Recipe.query.filter_by(recipe_name=recipe_name).first()
    if search_recipe:
        return search_recipe
    else:
        return None 
    
def get_recipe(recipe_id):
        return Recipe.query.get(recipe_id)
    
def list_all_recipes():
    recipe_list= Recipe.query.order_by(Recipe.recipe_id).all()
    if recipe_list:
        return recipe_list
    else:
        return None
    
def create_r_ingredient(recipe_id, ingredient_name):
    ingredient = Ingredients.query.filter_by(ingredient_name=ingredient_name).first()
    recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()

    if not ingredient:
        return False

    if recipe.ingredients == None or ingredient not in recipe.ingredients:
        recipe.ingredients.append(ingredient)
        db.session.add(recipe)
        db.session.commit()
    return True


def recipes_in_category(category_name):
    return Recipe.query.filter_by(category=category_name).all()
    