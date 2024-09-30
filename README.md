# Web Scraping Project

## Overview

This project is a simple web scraper that fetches and displays the text content of all paragraph (`<p>`) elements from a specified webpage. It utilizes the `requests` library to make HTTP requests and the `BeautifulSoup` library to parse and extract the desired information from the HTML.

## Requirements

To run this project, you need to have Python installed on your machine along with the following libraries:

- **requests**: For sending HTTP requests.
- **beautifulsoup4**: For parsing HTML content.

You can install these libraries using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

1. **Clone the repository** (if applicable) or create a new Python file and copy the provided code into it.
2. **Set the URL**: Update the `url` variable in the code to the webpage you want to scrape.
3. **Run the script**: Execute the script in your terminal or command prompt.

```bash
python your_script_name.py
```

## Code Explanation

Here's a brief explanation of the main components of the code:

- **Imports**: The script imports the `requests` library for making HTTP requests and `BeautifulSoup` from `bs4` for parsing HTML.
- **scrape_website(url)**: This function takes a URL as input, sends a GET request to the specified URL, and checks if the response is successful (status code 200).
- **HTML Parsing**: If the response is successful, the function uses BeautifulSoup to parse the HTML and find all paragraph (`<p>`) elements on the page.
- **Text Extraction**: The text content of each paragraph is printed to the console.

## Example

```python
url = 'https://techcrunch.com/2024/04/30/sams-clubs-ai-powered-exit-tech-reaches-20-of-stores/'
scrape_website(url)
```

## Output

The script will output the text content of all paragraphs found on the specified webpage.

## Troubleshooting

- If you encounter a status code other than 200, the script will print an error message indicating the failure.
- Ensure that the URL you are scraping is accessible and does not block requests from scripts.
