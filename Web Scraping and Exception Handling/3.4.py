import requests
from bs4 import BeautifulSoup
import csv

url = f'https://www.flipkart.com/search?q='
try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all the product listings (div elements with class "product")
        product_listings = soup.find_all('div', class_='product')
        
        # Create a CSV file to store the data
        with open('ecommerce_data.csv', 'w', newline='') as csvfile:
            # Define the CSV writer
            csv_writer = csv.writer(csvfile)
            
            # Write header row
            csv_writer.writerow(['Product Name', 'Price'])
            
            # Extract product names and prices from the product listings and write to CSV
            for product in product_listings:
                name = product.find('h2', class_='product-name').text
                price = product.find('span', class_='product-price').text
                
                # Write product data to the CSV file
                csv_writer.writerow([name, price])
                
        print("Data has been scraped and saved as 'ecommerce_data.csv'.")
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error:", e)
except Exception as e:
    print("An error occurred:", e)
