from App.models import Category
from App.database import db

def create_category( category_id, category_name, category_thumbnail):
    new_category = Category(category_id=category_id,   category_name=category_name,  category_thumbnail=category_thumbnail)
    db.session.add(new_category)
    db.session.commit()
    return new_category

def get_category_by_name(category_name):
    return Category.query.filter_by(category_name=category_name).first()

def get_category(category_id):
    return Category.query.get(category_id)

def get_all_users():
    return Category.query.all()