def filter_highly_rated_movies(movies):
    return [movie for movie in movies if movie.get('imdb_rating', 0) > 5.5]


movies = []
while True:
    title = input("'exit' to stop): ")
    if title.lower() == 'exit':
        break

    imdb_rating = float(input("Enter the IMDB rating: "))

    movie = {'title': title, 'imdb_rating': imdb_rating}
    movies.append(movie)

highly_rated_movies = filter_highly_rated_movies(movies)
print("Highly rated movies:", highly_rated_movies)
