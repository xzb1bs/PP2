def filter_movies_by_category(movies, category):
    return [movie for movie in movies if movie.get('category') == category]


movies = []
while True:
    title = input("'exit' to stop: ")
    if title.lower() == 'exit':
        break

    category = input()

    movie = {'title': title, 'category': category}
    movies.append(movie)

category = input()
filtered_movies = filter_movies_by_category(movies, category)
print(f"Movies in the category '{category}':", filtered_movies)
