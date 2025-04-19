from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from App.controllers import create_user, initialize
from App.controllers.recipe import list_all_recipes, get_recipe
from App.models.user import User

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', defaults={'recipe_id': None}, methods=['GET'])
@index_views.route('/<recipe_id>', methods=['GET'])
@jwt_required()
def index_page(recipe_id=None):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    recipe_list= list_all_recipes()
    selected_repcipe = get_recipe(recipe_id)
    if not selected_repcipe:
        selected_repcipe = None

    return render_template('index.html', recipe_list=recipe_list, selected_repcipe=selected_repcipe, user=user)

@index_views.route('/init', methods=['GET'])
def init():
    initialize()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})