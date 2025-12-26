# Write your solution here
def find_movies(database: list, search_term: str):
    result = []
    for movie in database:
        name: str = movie["name"]
        if name.lower().find(search_term.lower()) != -1:
            result.append(movie)
    return result
