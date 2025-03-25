#test comment RP

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {"title": title, "genre": genre, "rating": rating}
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie_dict in user_data["watchlist"]:
        print(movie_dict)
        if movie_dict["title"] == title:
            user_data["watchlist"].remove(movie_dict)
            user_data["watched"].append(movie_dict)
            break
        

    # if title in user_data["watchlist"]

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avr_rating(user_data):
    
    if "watched" in user_data:
        watched_movies = user_data["watched"]
    else:
        watched_movies = []
    
    if not watched_movies:
        return 0.0
    
    total_rating = 0
    movie_count = 0
    
    for movie in watched_movies:
        total_rating += movie["rating"]
        movie_count += 1
    avr_rating = total_rating / movie_count
    
    return avr_rating

def get_most_watched_genre(user_data):
    
    if "watched" not in user_data or user_data["watched"] == []:
        return None
    
    watched_movies = user_data["watched"]
    genre_count ={}

    for movie in watched_movies:
        genre = movie["genre"]
        
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
    
    # Find the most warched genre
    
    most_watched_genre = None
    max_count = 0 
    
    for genre, count in genre_count.items():
        
        if count > max_count:
            most_watched_genre = genre
            max_count = count
    
    return most_watched_genre
            
        
        
        
        
    



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def chat():
    print("Hello!!")