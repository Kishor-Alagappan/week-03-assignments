import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/Main_Page"
try:
    response = requests.get(url)    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')   
        links = soup.find_all('a')      
        for link in links:
            href = link.get('href')
            if href:
                print("Hyperlink:", href)
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error:", e)
except Exception as e:
    print("An error occurred:", e)
