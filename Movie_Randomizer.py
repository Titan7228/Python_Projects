from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import time
import random

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(service=FireFoxService(GeckoDriverManager().install()), options=options)

url = 'https://www.justwatch.com/us/provider/netflix/movies?genres=hrr&sort_by=title&sort_asc=true'
driver.get(url)


def scroll_to_bottom():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)


max_movie_count = 300  # Adjust this number as needed

movie_urls = []
while len(movie_urls) < max_movie_count:
    scroll_to_bottom()
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href and '/us/movie/' in href:
            movie_urls.append(href)
            if len(movie_urls) >= max_movie_count:
                break

if movie_urls:
    random_movie_url = random.choice(movie_urls)
    print('Random Movie URL:', random_movie_url)
else:
    print('No movie URLs found on this page')

driver.quit()
