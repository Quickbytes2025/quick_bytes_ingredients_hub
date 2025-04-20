
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from App.controllers.user import get_user
from App.models.r_user import R_user
from App.models.recipe import Recipe
from App.database import db

r_user_views = Blueprint('r_user_views', __name__, template_folder='../templates')

@r_user_views.route('/user/<int:user_id>/recipes', methods=['GET'])
def get_recipes(user_id):
    user = get_user(user_id)
    all_recipes = Recipe.query.all()
    my_recipes = []
    if user:
        my_recipes = (
            db.session.query(Recipe)
            .join(R_user, R_user.recipe_id == Recipe.recipe_id)
            .filter(R_user.user_id == user.id)
            .all()
        )    
    return render_template('user_recipes.html', my_recipes=my_recipes, all_recipes=all_recipes, user_id=user_id, user=user)

@r_user_views.route('/user/<int:user_id>/recipes/add', methods=['POST'])
def add_recipe(user_id):
    recipe_id = request.form.get('recipe_id')
    try:
        new_r_user = R_user(user_id=user_id, recipe_id=recipe_id)
        db.session.add(new_r_user)
        db.session.commit()
        flash('Recipe added successfully')
    except:
        flash('Failed to add recipe')
    return redirect(url_for('r_user_views.get_recipes', user_id=user_id))

@r_user_views.route('/user/<int:user_id>/recipes/remove/<int:recipe_id>', methods=['POST'])
def remove_recipe(user_id, recipe_id):
    try:
        R_user.query.filter_by(user_id=user_id, recipe_id=recipe_id).delete()
        db.session.commit()
        flash('Recipe removed successfully')
    except:
        flash('Failed to remove recipe')
    return redirect(url_for('r_user_views.get_recipes', user_id=user_id))
