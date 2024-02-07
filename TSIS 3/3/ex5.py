def average_imdb_score_by_category(movies, category):
    category_movies = [movie for movie in movies if movie.get('category') == category]
    
    if not category_movies:
        return 0 

    total_score = sum(movie.get('imdb_rating', 0) for movie in category_movies)
    average = total_score / len(category_movies)
    return average

movies = []
while True:
    title = input("'exit' to stop: ")
    if title.lower() == 'exit':
        break
    category = input()
    imdb_rating = float(input())
    movie = {'title': title, 'category': category, 'imdb_rating': imdb_rating}
    movies.append(movie)


category_to_average = input()

average_score = average_imdb_score_by_category(movies, category_to_average)
print(f"Average IMDB score for '{category_to_average}' movies: {average_score:.2f}")
