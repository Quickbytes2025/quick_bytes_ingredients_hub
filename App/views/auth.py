from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for,session
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies

from App.controllers.user import get_all_users


from.index import index_views

from App.controllers import (
    login
)

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')




'''
Page/Action Routes
'''    
@auth_views.route('/login', methods=['GET', 'POST'])
def login_action():
    if request.method == 'POST':
        data = request.form
        token = login(data['username'], data['password'])
        if not token:
            flash('Bad username or password given', 'error')
            return redirect(url_for('auth_views.login_action'))
        else:
            flash('Login Successful', 'success')
            response = redirect(url_for('index_views.index_page'))  # Redirect to the home page
            set_access_cookies(response, token)
            session['user'] = data['username']  # Store username in session
            return response

    # Render the login page for GET requests
    return render_template('login.html')

@auth_views.route('/logout', methods=['GET'])
def logout_action():
    response = redirect(url_for('auth_views.login_action'))  # Redirect back to the login page
    flash("Logged Out!", 'success')
    unset_jwt_cookies(response)
    session.pop('user', None)  # Remove user from session
    return response

'''
API Routes
'''

@auth_views.route('/api/login', methods=['POST'])
def user_login_api():
    data = request.json
    token = login(data['username'], data['password'])
    if not token:
        return jsonify(message='Bad username or password given'), 401
    response = jsonify(access_token=token) 
    set_access_cookies(response, token)
    return response

@auth_views.route('/api/identify', methods=['GET'])
@jwt_required()
def identify_user():
    return jsonify({'message': f"username: {current_user.username}, id : {current_user.id}"})

@auth_views.route('/api/logout', methods=['GET'])
def logout_api():
    response = jsonify(message="Logged Out!")
    unset_jwt_cookies(response)
    return response