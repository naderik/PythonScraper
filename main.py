from bs4 import BeautifulSoup
import requests

#search = input("Enter your job description: ")
#params = {"q": search}

URL = "https://ca.indeed.com/jobs?q=full+stack+developer&l=Canada"
r = requests.get(URL)
soup = BeautifulSoup(r.content, "html.parser")
results = soup.find(id='resultsCol')
jobs = results.findAll("div", class_="jobsearch-SerpJobCard unifiedRow row result")


if __name__ == '__main__':

    print('Web Scraping Started\n')

    for job in jobs:
        title = job.find('h2', class_='title')
        company = job.find('span', class_='company')
        location = job.find('div', class_='location accessible-contrast-color-location')
        if None in (title, company, location):
            continue
        print(title.text.strip())
        print(company.text.strip())
        print(location.text.strip())
        print()

