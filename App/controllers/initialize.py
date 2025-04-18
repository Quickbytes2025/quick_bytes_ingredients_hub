from flask import json

from .r_ingredients import create_r_ingredient
from .category import create_category
from .ingredients import create_ingredient
from .recipe import create_recipe
from .user import create_user
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    with open('ingredients.json') as file_I:
        data = json.load(file_I)
        ingredients_list = data['meals']

    for ingredient in ingredients_list:
        create_ingredient(ingredient['idIngredient'], ingredient['strIngredient'])
    

    with open('categories.json') as file_C:
        data = json.load(file_C)
        category_list = data['categories']

    for category in category_list:
        create_category(category['idCategory'], category['strCategory'], category['strCategoryDescription'], category['strCategoryThumb'])

    with open('recipes.json') as file_R:
        recipe_details_data = json.load(file_R)
        recipe_list = recipe_details_data['meals']
         
    for recipe_detail in recipe_list:
        create_recipe(recipe_detail['idMeal'], recipe_detail['strMeal'], recipe_detail['strInstructions'], recipe_detail['strMealThumb'], recipe_detail['strYoutube'], recipe_detail['strCategory'])
        string = "strIngredient"
        i = 1

        while recipe_detail[f'{string + str(i)}'] != None and recipe_detail[f'{string + str(i)}'] != "":
            create_r_ingredient(recipe_detail['idMeal'], recipe_detail[f'{string + str(i)}'], f'{str(i)}')
            i = i + 1
            if i == 21:
                break

    create_user('bob', 'bobpass')

