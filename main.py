from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
data = response.text

soup = BeautifulSoup(data, "html.parser")

all_movies = [movie.get_text() for movie in soup.find_all(name="h3", class_="title")]
reversed_movies = all_movies[::-1]

with open("movies.txt", "w") as f:
    for movie in reversed_movies:
        f.write(f"{movie}\n")

print(reversed_movies)
