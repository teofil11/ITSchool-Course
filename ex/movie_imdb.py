import requests
from bs4 import BeautifulSoup
import csv

def rating_movies():
    url = 'https://www.cinemagia.ro/liste/best-movies-5117/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = []
    try:
        for movie in soup.find_all('div', class_ = 'subtitle'):
            title = movie.text
            rating = movie.find_next('span', class_ = 'text_big').text  
            if float(rating) > 8.0:
                movies.append([title, rating])

    except AttributeError:
        pass

    return movies

def write_movies():
    movies = rating_movies()
    header = ['Movie', 'Rating']
    with open('ex/test/movies_2023.csv', 'w',newline= '', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(movies)

write_movies()
