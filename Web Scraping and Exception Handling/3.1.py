import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com"
try:
    response = requests.get(url)    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')        
        title = soup.title.string        
        print("Title:", title)
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error:", e)
except Exception as e:
    print("An error occurred:", e)
