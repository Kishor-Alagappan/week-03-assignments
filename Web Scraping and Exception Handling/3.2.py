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
