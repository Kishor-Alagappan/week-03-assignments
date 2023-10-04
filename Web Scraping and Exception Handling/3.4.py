import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

print('Enter the product name below to fetch its different variants and prices: ')
prod = input().split()
search_query = '+'.join(prod)
url = f'https://www.flipkart.com/search?q={search_query}'

try:
    response = requests.get(url)
    time.sleep(2)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        names = [element.text for element in soup.find_all('div', class_='_4rR01T')]
        time.sleep(2)
        prices = [element.text for element in soup.find_all('div', class_='_30jeq3 _1_WHN1')]
        df = pd.DataFrame({'Product_name': names, 'Product_price': prices})
        df.to_csv('products.csv', index=False)
        print('Content successfully saved to .csv file')
    else:
        print(f'Unknown response code {response.status_code} for URL: {url}')
except Exception as e:
    print(f'An error occurred: {e}')