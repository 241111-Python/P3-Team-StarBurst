class swiftData:
    def __init__(
        self,
        Title,
        Published,
        Duration,
        View_Count
    ):
        self.Title = Title
        self.Published = Published
        self.Duration = Duration
        self.View_Count = int(View_Count)

    def __str__(self):
        return f"{self.Published} - {self.View_Count}"
