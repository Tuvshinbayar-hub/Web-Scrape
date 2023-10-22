import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import lxml
URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

# Set up the Microsoft Edge WebDriver
options = webdriver.EdgeOptions()
options.add_argument('--headless')  # Run Edge in headless mode (no GUI)
driver = webdriver.Edge(options=options)

# Load the URL and wait for the page to fully render
driver.get(URL)
driver.implicitly_wait(10)

content = driver.page_source
soup = BeautifulSoup(content, 'lxml')

all_titles = soup.select('.listicle-item h3')
all_names = [title.string for title in all_titles]
all_names.reverse()
all_names = [name+'\n' for name in all_names]


def save_locally(movie_names: list):
    with open('movies.txt', mode='w') as data:
        data.writelines(movie_names)


save_locally(all_names)

