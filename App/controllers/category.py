from App.models import Category
from App.database import db

def create_category( category_id, category_name, category_thumbnail):
    new_category = Category(category_id=category_id,   category_name=category_name,  category_thumbnail=category_thumbnail)
    db.session.add(new_category)
    db.session.commit()
    return new_category

def get_category_by_name(category_name):
    category_search = Category.query.filter_by(category_name=category_name).first()
    if category_search:
        return category_search
    else:
        return None


def get_category(category_id):
    selected_category= Category.query.get(category_id)
    if selected_category:
        return selected_category
    else:
        return None 

def list_all_categories():
    category_list=Category.query.all()
    if category_list:
        return category_list
    else:
        return None