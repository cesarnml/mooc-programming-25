# Write your solution here


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
        recipe_map[name] = {"name": name, "time": time, "ingredients": recipe[2:]}
    return recipe_map


def search_by_time(filename: str, time: int):
    recipe_map = read_file(filename)
    found_recipe = []
    for recipe in recipe_map:
        current_recipe = recipe_map[recipe]
        if current_recipe["time"] <= time:
            found_recipe.append(
                f'{current_recipe["name"]}, preparation time {current_recipe["time"]} min'
            )
    return found_recipe


def search_by_ingredient(filename: str, ingredient: str):
    recipe_map = read_file(filename)
    found_recipe = []
    for recipe in recipe_map:
        current_recipe = recipe_map[recipe]
        ingredients = [x.lower() for x in current_recipe["ingredients"]]
        if ingredient.lower() in ingredients:
            found_recipe.append(
                f'{current_recipe["name"]}, preparation time {current_recipe["time"]} min'
            )
    return found_recipe


# print(search_by_ingredient("recipes1.txt", "eggs"))
# print(search_by_name("recipes1.txt", "cake"))
# print(search_by_time("recipes1.txt", 20))
