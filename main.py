'''Requirements
requests library (install using pip install requests)
beautifulsoup4 library (install using pip install beautifulsoup4)'''


import requests
from bs4 import BeautifulSoup

# Scraper function
def scrape_website(url):
    response = requests.get(url)#The scrape_website function sends a GET request to the specified URL using requests.get()

    if response.status_code == 200:#None (prints an error message if the response status code is not 200)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')#It finds all <p> elements (paragraphs) on the webpage using soup.find_all('p').
        for para in paragraphs:

            print(para.get_text())#It iterates over the paragraphs and prints the text content of each paragraph using para.get_text().'''
    else:
        print(f"Failed to scrape the website Status code: {response.status_code}")

#url (str): The URL of the webpage to scrape.
url = 'https://techcrunch.com/2024/04/30/sams-clubs-ai-powered-exit-tech-reaches-20-of-stores/'

# Call the function to scrape and print content
scrape_website(url)


