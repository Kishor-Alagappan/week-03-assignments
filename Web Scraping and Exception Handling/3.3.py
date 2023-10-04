import requests
from bs4 import BeautifulSoup

url = input('Enter an URL of your choice : ')
try:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            print(href)
    else:
        print(f'Invalid response code {response.status_code} for : {url}')
except:
    print(f'Invalid webpage : {url}')