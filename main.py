from bs4 import BeautifulSoup
import requests

#search = input("Enter your job description: ")
#params = {"q": search}

URL = "https://ca.indeed.com/jobs?q=full+stack+developer&l=Canada"
r = requests.get(URL)
soup = BeautifulSoup(r.content, "html.parser")
results = soup.find(id='resultsCol')
jobs = results.find_all('div', class_="jobsearch-SerpJobCard unifiedRow row result clickcard")

for job in jobs:
    print(job, end='\n'*2)


if __name__ == '__main__':
    print('Web Scraping Started')

    # for item in links:
    # item.text = item.find("a").text
    # item.href = item.find("a").attrs["href"]

    # if item.text and item.href:
    #  print(item.text)
    #  print(item.href)
