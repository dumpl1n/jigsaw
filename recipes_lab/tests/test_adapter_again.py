from tests.test_adapter import sample_meals
from src.adapter import meal_names, meal_ids

# meal names test
def test_meal_names():
    all_meal_names = meal_names(sample_meals)
    assert all_meal_names == ['Brown Stew Chicken', 'Chicken & mushroom Hotpot', 'Chicken Alfredo Primavera', 'Chicken Basquaise', 'Chicken Congee', 'Chicken Handi', 'Kentucky Fried Chicken', 'Kung Pao Chicken', 'Pad See Ew', 'Piri-piri chicken and slaw', 'Thai Green Curry']
# meal ids test

#'idMeal'
def test_meal_ids():
    all_meal_ids = meal_ids(sample_meals)
    assert all_meal_ids == ['52940', '52846', '52796', '52934', '52956', '52795', '52813', '52945', '52774', '53039', '52814']