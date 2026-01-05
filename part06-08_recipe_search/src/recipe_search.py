# Write your solution here
from re import S


def search_by_name(filename: str, name: str):
    recipe_map = read_file(filename)
    matches = []
    for recipe in recipe_map:
        if name.lower() in recipe.lower():
            matches.append(recipe)
    return matches


def read_file(filename: str):
    recipes = []
    with open(filename) as file:
        current_recipe = []
        for line in file:
            if line == "\n":
                recipes.append(current_recipe)
                current_recipe = []
            else:
                current_recipe.append(line.strip())
    recipes.append(current_recipe)
    return create_recipe_map(recipes)


def create_recipe_map(recipes):
    recipe_map = {}
    for recipe in recipes:
        name = recipe[0]
        time = int(recipe[1])
        recipe_map[name] = {}
        recipe_map[name]["name"] = name
        recipe_map[name]["time"] = time
        recipe_map[name]["ingredients"] = recipe[2:]
    return recipe_map


# print(search_by_name("recipes1.txt", "cake"))
