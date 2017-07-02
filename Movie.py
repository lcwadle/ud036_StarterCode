class Movie():
    def __init__(self, title, description, release_date, cast, directors, trailer_youtube_url, poster_image_url, reviews):
        self.title = title
        self.description = description
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.release_date = release_date
        self.cast = cast
        self.reviews = reviews
        self.directors = directors
