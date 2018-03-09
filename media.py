import webbrowser


class Movie():
    """This class provides a way to store movie related information

    Attributes:
        movie_title (str): stores title of the movie
        movie_storyline (str): stores movie storyline
        poster_image (str): stores url of the poster image
        trailer_youtube (str): stores url to the trailer from youtube

    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Print title of the movies
    def get_title(self):
        print(self.title)

    # Print storyline of the movies
    def get_storyline(self):
        print(self.storyline)

    # Open poster image of the movies
    def show_poster_image(self):
        webbrowser.open(self.poster_image_url)

    # Open movie trailer in browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
