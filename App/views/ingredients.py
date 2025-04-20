from flask import Blueprint, jsonify
from App.models.ingredients import Ingredients

ingredient_views = Blueprint('ingredient_views', __name__, template_folder='../templates')

@ingredient_views.route('/ingredients', methods=['GET'])
def get_all_ingredients():
    ingredients = Ingredients.query.all()
    return jsonify([ingredient.get_json() for ingredient in ingredients])