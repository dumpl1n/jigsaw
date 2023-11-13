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

