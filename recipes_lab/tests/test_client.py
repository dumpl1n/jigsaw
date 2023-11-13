import sys
sys.path.append("/Users/kielay/code/jigsaw/recipes_lab")
import requests
from src.client import recipe_url, main_ingredients, request_by_recipe, request_by_main_ingredient, id_url

def test_recipe_url_returns_the_url_to_search_by_meal_name():
    meal_name = 'pizza'
    assert recipe_url(meal_name) == "https://www.themealdb.com/api/json/v1/1/search.php?s=pizza"

def test_main_ingredient_url_returns_the_url_to_search_by_ingredient():
    main_ingredient = 'chicken'
    assert main_ingredients(main_ingredient) == 'https://www.themealdb.com/api/json/v1/1/filter.php?i=chicken'
    
def test_request_by_recipe():
    results = request_by_recipe('pizza')
    assert results['meals'][0]['strMeal'] == 'Pizza Express Margherita'

def test_request_by_main_ingredient():
    results = request_by_main_ingredient('cheese')
    assert results['meals'][0]['strMeal'] == 'Big Mac'

def test_request_id_url(): #added this test
    results = id_url('52772')
    assert results == 'https://www.themealdb.com/api/json/v1/1/lookup.php?i=52772'

#this needs to be revisited
def test_request_by_id():
    results = requests.get(id_url('52772')).json() #added requests.get and .json() to get to pass
    assert results['meals'][0]['idMeal'] == '52772'