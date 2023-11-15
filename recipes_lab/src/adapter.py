from .client import request_by_recipe

# meal_recipe -
# Write a function that takes the name of a meal 
# and then hits the api to returns just the text of the corresponding recipe. 
# This should use the request_by_recipe function.
def meal_recipe(name:str)-> str:
    response = request_by_recipe(name)['meals'][0]['strInstructions']
    return response


# meal_names - 'strMeal'
# _and_ids -  'idMeal'
# Write a function that takes a list of sample meals and returns just the name and id of each meal. 
# Look at the tests to see how this works. You can copy the sample_meals variable into the console to work with this.
def meal_names_and_ids(meals:list)-> list:
    output = []
    for meal in meals:
        output.append({'name':meal['strMeal'], 'id':meal['idMeal']})
    return output


def meal_names(sample_meals):
    all_meal_names = [meal['strMeal'] for meal in sample_meals]
    return all_meal_names

def meal_ids(sample_meals):
    all_meal_ids = [meal['idMeal'] for meal in sample_meals]
    return all_meal_ids

# takes in a single meal and returns a list of ingredients
def find_ingredients_from(sample_meal):
    keys = [f'strIngredient{i}' for i in range(1,21) if sample_meal[f'strIngredient{i}']]
    output = []
    for key in keys:
        output.append(sample_meal[key])  
    return output

#Write a function that takes a single meal and returns a dictionary
# where the keys are the ingredients and the value is each corresponding measuremment needed
def find_ingredient_measurements(sample_meal):
    ingredient = [sample_meal[f'strIngredient{i}'] for i in range(1,21) if sample_meal[f'strIngredient{i}']]
    measure = [sample_meal[f'strMeasure{i}'] for i in range(1,21) if sample_meal[f'strMeasure{i}']]
    # output = dict()
    # for key, i in enumerate(ingredient):
    #     sample_meal[ingredient[i]] = sample_meal[measure[i]]
    return dict(zip(ingredient, measure))

