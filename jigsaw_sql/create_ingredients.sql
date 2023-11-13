-- create_ingredients.sql
CREATE TABLE ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    cost_per_ounce FLOAT,
    calories_per_ounce INTEGER,
    expiration DATE);