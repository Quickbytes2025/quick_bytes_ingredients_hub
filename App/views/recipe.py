from flask import Blueprint, render_template, jsonify, request, flash, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies

from.index import index_views

from App.controllers import (
    recepies_in_category,
    get_category_by_name,
    get_recipe,
    list_all_recipes,
    jwt_required
)

recipe_views = Blueprint('recipe_views', __name__, template_folder='../templates')

@recipe_views.route('/render-recipes/<name>', methods=['GET'])
def get_recipe_page(name):
    select_category = get_category_by_name(name)
    if select_category:
        recipe_list = recepies_in_category(select_category.name)
        if recipe_list:
            return render_template('recipes.html', recipe_list=recipe_list, category = select_category.name)
            
        else:
            print("{select_category.name} recipes do not exist here")
            
            return jsonify({'message': f'{select_category.name}  recipes do not exist here'})
    else:
        print("Category does not exist")
    return redirect(url_for('user_views.get_categories_page'))


@recipe_views.route('/render-details/<string:name>', methods=['GET'])
def get_details_page(name):
    selected_category = get_category_by_name(name)
    if selected_category:
        return render_template('details.html', item_details=selected_category)
    else:
        selected_recipe = get_recipe(name)
        if selected_recipe:
            return render_template('details.html', item_details=selected_recipe)
    return redirect(url_for('user_views.get_categories_page'))


@recipe_views.route('/render-all-recipes', methods=['GET'])
def list_all_recipes_page():
    recipes_list = list_all_recipes()
    if recipes_list:
        return render_template('recipes.html', recipes_list=recipes_list)
    return redirect(url_for('user_views.get_categories_page'))