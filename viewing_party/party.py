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


    print(new_movies)
    return new_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# def chat():
#     print("Hello!!")