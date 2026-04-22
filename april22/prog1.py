reviews = [
  {"movie": "Inception",  "user": "alice", "rating": 9},
  {"movie": "Dune",       "user": "bob",   "rating": 8},
  {"movie": "Inception",  "user": "bob",   "rating": 7},
  {"movie": "Interstellar","user":"alice",  "rating": 10},
  {"movie": "Dune",       "user": "charlie","rating": 9},
  {"movie": "Interstellar","user":"charlie","rating": 8},
]

# 1. Group reviews by movie
movie_dict = {}

for r in reviews:
    movie = r["movie"]
    rating = r["rating"]
    
    if movie not in movie_dict:
        movie_dict[movie] = []
    
    movie_dict[movie].append(rating)

# 2. Average ratings
avg_ratings = {}
for movie, ratings in movie_dict.items():
    avg_ratings[movie] = sum(ratings) / len(ratings)

# 3. Top movie
top_movie = max(avg_ratings, key=avg_ratings.get)

# 4. Must watch (>= 8.5)
must_watch = [movie for movie, avg in avg_ratings.items() if avg >= 8.5]

# 5. User favourites
user_favs = {}

for r in reviews:
    user = r["user"]
    movie = r["movie"]
    rating = r["rating"]
    
    if user not in user_favs or rating > user_favs[user][1]:
        user_favs[user] = (movie, rating)

# remove rating, keep only movie
user_favs = {user: val[0] for user, val in user_favs.items()}

# OUTPUT
print("avg_ratings =", avg_ratings)
print("top_movie =", top_movie)
print("must_watch =", must_watch)
print("user_favs =", user_favs)