import requests
from bs4 import BeautifulSoup

url = input('Enter a url of your choice : ')
try:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string
        print('')
        print(f'Title of {url} is {title}')
    else:
        print('')
        print(f'Unknown response code : {response.status_code}')
except:
    print('')
    print('Error! No such webpage')