import media
import fresh_tomatoes
import json
import requests
import config

# API key for OMDb.com
API_KEY = config.api_key

# Return URL for movie database API
def get_movie_data(movie):
    url = "http://www.omdbapi.com/?t=" + movie + "&apikey=" + API_KEY + "&r=json"
    return url


# Create Die Hard database
response = requests.get(get_movie_data("die_hard"))
data = json.loads(response.text)
die_hard = media.Movie(data.get("Title"),
                        data.get("Plot"),
                        data.get("Poster"),
                        "https://www.youtube.com/watch?v=2TQ-pOvI6Xo")

# Create Osmosis Jones database
response = requests.get(get_movie_data("osmosis_jones"))
data = json.loads(response.text)
osmosis_jones = media.Movie(data.get("Title"),
                        data.get("Plot"),
                        data.get("Poster"),
                        "https://www.youtube.com/watch?v=CJ5Pkibjbv0")

# Create Inception database
response = requests.get(get_movie_data("inception"))
data = json.loads(response.text)
inception = media.Movie(data.get("Title"),
                        data.get("Plot"),
                        data.get("Poster"),
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

# Create Interstellar database
response = requests.get(get_movie_data("interstellar"))
data = json.loads(response.text)
interstellar = media.Movie(data.get("Title"),
                        data.get("Plot"),
                        data.get("Poster"),
                        "https://www.youtube.com/watch?v=0vxOhd4qlnA")

# Create Star Wars: The Last Jedi database
response = requests.get(get_movie_data("star_wars_the_last_jedi"))
data = json.loads(response.text)
star_wars_viii = media.Movie(data.get("Title"),
                        data.get("Plot"),
                        data.get("Poster"),
                        "https://www.youtube.com/watch?v=Q0CbN8sfihY")

# Create Ready Player One database
response = requests.get(get_movie_data("ready_player_one"))
data = json.loads(response.text)
ready_player_one = media.Movie(data.get("Title"),
                        data.get("Plot"),
                        data.get("Poster"),
                        "https://www.youtube.com/watch?v=cSp1dM2Vj48")


# Put all movies database in a list
movies = [die_hard, osmosis_jones, inception, interstellar, star_wars_viii,
        ready_player_one]

# Create movie page
fresh_tomatoes.open_movies_page(movies)
