from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user 

from.index import index_views

from App.controllers import (
    list_all_categories,
    get_category,
    recepies_in_category,
    jwt_required
)

category_views = Blueprint('category_views', __name__, template_folder='../templates')

@category_views.route('/categories', methods=['GET'])
@jwt_required()
def get_categories_page():
    categories = list_all_categories()
    flash(f"Categories")
    return render_template('categories.html', categories=categories, category_detail=None)