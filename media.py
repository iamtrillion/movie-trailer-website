import webbrowser

class Video():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    """This class provides a way to define all other subclasses beneath it"""
    def __init__(self, video_title, video_duration):
        self.title = video_title
        self.duration = video_duration
        
class Movie(Video):
    """This class provides a way to store movie related information"""
    def __init__ (self, video_title, video_duration, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, video_title, video_duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
    
class TvShow(Video):
    """Several Tv Shows"""
    def __init__(self, video_title, video_duration, series_storyline, series_image, series_url):
        Parent.__init__(self, video_title, video_duration)
        self.storyline = series_storyline
        self.image = series_image
        self.url = series_url
        
        
