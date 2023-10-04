# import requests
# from bs4 import BeautifulSoup

# url = input('Enter a url of your choice : ')
# try:
#     response = requests.get(url)
#     if response.status_code == 200:
#         print('')
#         print(f'Response code from the webpage {url} is {response.status_code}')
#         print('')
#         print('Content of the webpage is : ')
#         print(response.text)
#     else:
#         print('')
#         print(f'Something wrong with the webpage, response code is {response.status_code}')
# except:
#     print('')
#     print('Invalid webpage') 


import requests

# URL of the webpage you want to fetch
url = "https://www.google.com"

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Print the status code of the response
    print("Status Code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error:", e)
except Exception as e:
    print("An error occurred:", e)
