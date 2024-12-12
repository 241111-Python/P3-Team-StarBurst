class spotifyData:
    def __init__(
        self,
        Title,
        Artist,
        Genre,
        Year,
        BPMinute,
        Energy,
        Danceability,
        Loudness,
        Liveness,
        Valence,
        Length,
        Acousticness,
        Speechiness,
        Popularity
    ):
        self.Title = Title
        self.Artist = Artist
        self.Genre = Genre
        self.Year = int(Year)
        self.BPMinute = BPMinute
        self.Energy = Energy
        self.Danceability = Danceability
        self.Loudness = Loudness
        self.Valence = Valence
        self.Length = Length
        self.Acousticness = Acousticness
        self.Speechiness = Speechiness
        self.Popularity = int(Popularity)
        
        def __str__(self):
            return f"{self.Artist}: {self.Year} - {self.Popularity}"
