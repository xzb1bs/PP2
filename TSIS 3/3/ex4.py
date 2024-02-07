def average_imdb_score(movies):
    if not movies:
        return 0  
    total_score = sum(movie.get('imdb_rating', 0) for movie in movies)
    average = total_score / len(movies)
    return average

movies = []
while True:
    title = input("'exit' to stop: ")
    if title.lower() == 'exit':
        break

    imdb_rating = float(input("IMDB rating: "))
    movie = {'title': title, 'imdb_rating': imdb_rating}
    movies.append(movie)

average_score = average_imdb_score(movies)
print(f"Average IMDB score of movies: {average_score:.2f}")
