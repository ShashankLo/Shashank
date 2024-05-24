import requests
from bs4 import BeautifulSoup

def simple_web_scraper(url):
    # Send a GET request to the URL
    response = requests.get(url='https://flipkart.com')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract information based on HTML tags - adjust as per your needs
        titles = soup.find_all('h2')

        # Print or store the extracted data
        for title in titles:
            print(title.text)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Replace 'https://flipkart.com' with the URL you want to scrape
url_to_scrape = 'https://flipkart.com'
simple_web_scraper(url_to_scrape)
