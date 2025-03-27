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
    # print(user_data)
    for movie_dict in user_data["watchlist"]:
        print(movie_dict)
        if movie_dict["title"] == title:
            user_data["watchlist"].remove(movie_dict)
            user_data["watched"].append(movie_dict)
            break


    # if title in user_data["watchlist"]

    # print(user_data)
    return user_data



# janes_data = {
#     "watchlist": [{
#     "title": "MOVIE_TITLE_1",
#     "genre": "GENRE_1",
#     "rating": "RATING_1"
#     }],
#     "watched": []
#     }

#     # Act
# watch_movie(janes_data, "MOVIE_TITLE_1")



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

def get_unique_watched(user_data):
    # for mov in user_data["watched"]:
    #     print(mov["title"]) #will get each movie title watched

    full_friends_movies = []
    for friend_list in user_data["friends"]:
        for friend_mov in friend_list["watched"]:
            # print(friend_mov["title"]) #will get each movie title
            full_friends_movies.append(friend_mov["title"])
        print("break")


    new_movies = []
    for mov in user_data["watched"]:
        if mov["title"] not in full_friends_movies:
            new_movies.append(mov)

    print(new_movies) #will get each movie title watched
    return new_movies



def get_friends_unique_watched(user_data):
    full_user_movies = []
    for mov in user_data["watched"]:
        full_user_movies.append(mov["title"])

    new_movies = []
    for friend_list in user_data["friends"]:
        for friend_mov in friend_list["watched"]:
            if (friend_mov["title"] not in full_user_movies) and (friend_mov not in new_movies):
                new_movies.append(friend_mov)


    # print(new_movies)
    return new_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    rec_movies = []
    unwatched = get_friends_unique_watched(user_data)
    
    for movie in unwatched:
        if movie["host"] in user_data["subscriptions"]:
            rec_movies.append(movie)

    return rec_movies






# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    
    most_watched_genre = get_most_watched_genre(user_data)
    
    if most_watched_genre is None:
        return []
    
    recomendations = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie["genre"] == most_watched_genre and movie not in recomendations:
                recomendations.append(movie)
    
    return recomendations
            
            
def get_rec_from_favorites(user_data):
    
    if "favorites" not in user_data or user_data["favorites"] == []:
        return []
    
    recomendations = []
    friends_recomendations_list = []
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_recomendations_list.append(movie)
        
    for movie in user_data["favorites"]:
        if not movie in friends_recomendations_list:
            recomendations.append(movie)
            
    return recomendations
            
    
        
    
    

    



