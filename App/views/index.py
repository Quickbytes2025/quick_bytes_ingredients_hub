from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize
from App.controllers.recipe import get_all_recipes, get_recipe

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page(recipe_id=None):

    recipe_list= get_all_recipes()
    selected_repcipe = get_recipe(recipe_id)
    if not selected_repcipe:
        selected_repcipe = get_recipe(None)

    return render_template('index.html', recipe_list=recipe_list, selected_repcipe=selected_repcipe)

@index_views.route('/init', methods=['GET'])
def init():
    initialize()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})