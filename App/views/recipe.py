from flask import Blueprint, render_template, jsonify, request, flash, send_from_directory, flash, redirect, session, url_for
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies
from App.database import db
from App.controllers.user import get_user
from App.models.i_user import I_user
from App.models.ingredients import Ingredients



from.index import index_views

from App.controllers import (
    recipes_in_category,
    get_category_by_name,
    get_recipe,
    list_all_recipes,
    jwt_required
)

recipe_views = Blueprint('recipe_views', __name__, template_folder='../templates')

@recipe_views.route('/recipes/<category_name>', methods=['GET'])
def recipes_by_category(category_name):
    
    recipe_list = recipes_in_category(category_name)
    if recipe_list:
        return render_template('recipe.html', recipe_list=recipe_list, category_name=category_name)
            
    else:
        return jsonify({'message': f'{category_name}  recipes do not exist here'})
    


@recipe_views.route('/recipe/<recipe_id>', methods=['GET'])
def get_recipe_instructions(recipe_id):
    
    search_recipe = get_recipe(recipe_id)
    if search_recipe:
        user_id = None
        if 'user' in session:
            user_id = session['user']

        missing_ingredients = []
        if user_id:
            user = get_user(user_id)
            if user:
                user_ingredients = (db.session.query(Ingredients).join(I_user, I_user.ingredient_id == Ingredients.ingredient_id).filter(I_user.user_id == user.id).all())
                user_ingredient_ids = {i.ingredient_id for i in user_ingredients}
                recipe_ingredient_ids = {i.ingredient_id for i in search_recipe.ingredients}
                missing_ingredients = [i for i in search_recipe.ingredients if i.ingredient_id not in user_ingredient_ids]

        return render_template('recipe.html', search_recipe=search_recipe, recipe_id=recipe_id, missing_ingredients=missing_ingredients)    
    else:
        return jsonify({'message': f' recipe does not exist here'})


@recipe_views.route('/render-all-recipes', methods=['GET'])
def list_all_recipes_page():
    recipes_list = list_all_recipes()
    if recipes_list:
        return render_template('recipes.html', recipes_list=recipes_list)
    return redirect(url_for('user_views.get_categories_page'))