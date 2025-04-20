from App.models import User,Ingredients
from App.database import db

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    
def add_ingredient_to_user(user_id, ingredient_name):
    user = get_user(user_id)
    ingredient = Ingredients.query.get(ingredient_name)
    if user and ingredient:
        if ingredient not in user.ingredients:
            user.ingredients.append(ingredient)
            db.session.commit()
            return True
    return False

def remove_ingredient_from_user(user_id, ingredient_name):
    user = get_user(user_id)
    ingredient = Ingredients.query.get(ingredient_name)
    if user and ingredient:
        if ingredient in user.ingredients:
            user.ingredients.remove(ingredient)
            db.session.commit()
            return True
    return False

def get_user_ingredients(user_id):
    user = get_user(user_id)
    if user:
        return [ingredient.get_json() for ingredient in user.ingredients]
    return []
