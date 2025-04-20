from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from App.controllers.user import add_ingredient_to_user, get_user, remove_ingredient_from_user, get_user_ingredients
from App.models.i_user import I_user
from App.models.ingredients import Ingredients
from App.database import db

i_user_views = Blueprint('i_user_views', __name__, template_folder='../templates')

@i_user_views.route('/user/<int:user_id>/ingredients', methods=['GET'])
def get_ingredients(user_id):
    user= get_user(user_id)
    all_ingredients = Ingredients.query.all()
    my_ingredients = []
    if user:
          my_ingredients = (
            db.session.query(Ingredients)
            .join(I_user, I_user.ingredient_id == Ingredients.ingredient_id)
            .filter(I_user.user_id == user.id)
            .all()
        )    
    return render_template('user_ingredients.html', my_ingredients=my_ingredients, all_ingredients=all_ingredients, user_id=user_id, user=user)


@i_user_views.route('/user/<int:user_id>/ingredients/add', methods=['POST'])
def add_ingredient(user_id):
    ingredient_id = request.form.get('ingredient_id')
    if add_ingredient_to_user(user_id, ingredient_id):
        flash('Ingredient added successfully')
        return redirect(url_for('i_user_views.get_ingredients', user_id=user_id))
    flash('Failed to add ingredient')
    return redirect(url_for('i_user_views.get_ingredients', user_id=user_id))

@i_user_views.route('/user/<int:user_id>/ingredients/remove/<int:ingredient_id>', methods=['POST'])
def remove_ingredient(user_id, ingredient_id):
    if remove_ingredient_from_user(user_id, ingredient_id):
        flash('Ingredient removed successfully')
        return redirect(url_for('i_user_views.get_ingredients', user_id=user_id))
    flash('Failed to remove ingredient')
    return redirect(url_for('i_user_views.get_ingredients', user_id=user_id))