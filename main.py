from bs4 import BeautifulSoup
import requests

search = input("Enter search term: ")
params = {"q": search}
r = requests.get("https://google.com", params=params)

soup = BeautifulSoup(r.text, "html.parser")

if __name__ == '__main__':
    print('Web Scraping Started')
    print(soup.prettify())

