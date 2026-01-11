# Write your solution here:
class Series:
    def __init__(self, title: str, season_no: int, genres: list[str]):
        self.title = title
        self.season_no = season_no
        self.genres = genres
        self.ratings: list[int] = []

    def __str__(self):
        genres_str = ", ".join(self.genres)
        if len(self.ratings) == 0:
            rating_str = "no ratings"
        else:
            count = len(self.ratings)
            avg = sum(self.ratings) / count
            rating_str = f"{count} ratings, average {avg:.1f} points"
        return f"{self.title} ({self.season_no} seasons)\ngenres: {genres_str}\n{rating_str}"

    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.ratings.append(rating)


def minimum_grade(rating: float, series_list: list):
    return [
        series
        for series in series_list
        if len(series.ratings) > 0
        and sum(series.ratings) / len(series.ratings) >= rating
    ]


def includes_genre(genre: str, series_list: list):
    return [series for series in series_list if genre in series.genres]
