# `recipe_url` - Take a look at how to `Search a meal by name` in the documentation.  
# This method allows us to pass in the name of a recipe, and returns the appropriate url.  
import requests 

def recipe_url(name):
    return f'https://www.themealdb.com/api/json/v1/1/search.php?s={name}'


# `main_ingredient_url` - 
# Look at how to filter by main ingredient in the documentation.  
# Write a function that takes in a main ingredient, and returns the appropriate url.
def main_ingredients(ingredient):
    return f'https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}'


# * `request_by_recipe` - 
# Takes in a meal name, and then makes a request to the api to return the recipe for the related meal.  
# (Remember to use the console to check your work).  And of course, run the tests.
def request_by_recipe(name):
    response = requests.get(recipe_url(name))
    return response.json()



# * `request_by_main_ingredient` - 
# Takes in an ingredient name, and then makes a request to the api to return the a list of related recipes.
def request_by_main_ingredient(name):
    response = requests.get(main_ingredients(name))
    return response.json()

# * `id_url` - Takes in an id, and returns the url to search by id.
def id_url(id):
    return f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}'

