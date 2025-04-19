from flask import Blueprint, render_template, jsonify, request, flash, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies



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
        return render_template('recipe.html', search_recipe=search_recipe, recipe_id=recipe_id)
            
    else:
        return jsonify({'message': f' recipe does not exist here'})


@recipe_views.route('/render-all-recipes', methods=['GET'])
def list_all_recipes_page():
    recipes_list = list_all_recipes()
    if recipes_list:
        return render_template('recipes.html', recipes_list=recipes_list)
    return redirect(url_for('user_views.get_categories_page'))