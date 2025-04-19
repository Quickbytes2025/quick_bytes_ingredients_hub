from App.models import Ingredients
from App.database import db


def create_ingredient(ingredient_id,ingredient_name):
    new_ingredient = Ingredients(ingredient_id=ingredient_id, ingredient_name=ingredient_name)
    db.session.add(new_ingredient)
    db.session.commit()
    return new_ingredient

def get_ingredient_by_username(ingredient_name):
    ingredient_search= Ingredients.query.filter_by(ingredient_name).first()
    if ingredient_search:
        return ingredient_search
    else:
        return None 
    
    
def get_ingredient(ingredient_id):
    selected_ingredient= Ingredients.query.get(ingredient_id)
    if selected_ingredient:
        return selected_ingredient
    else:
        return None 
    
    

def get_all_ingredients():
    ingredient_list=Ingredients.query.all()
    if ingredient_list:
        return ingredient_list
    else:
        return None 
    