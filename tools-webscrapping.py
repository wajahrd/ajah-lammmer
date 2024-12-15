import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP requests with status codes 4xx or 5xx

        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Extract all text within <h1> tags
        h1_tags = [h1.get_text(strip=True) for h1 in soup.find_all('h1')]

        # Example: Extract all links (URLs) from the webpage
        links = [a['href'] for a in soup.find_all('a', href=True)]

        # Return the extracted data
        return {
            'h1_tags': h1_tags,
            'links': links
        }

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

if __name__ == "__main__":
    # Example: URL to scrape
    url = "https://www.urewebsite.com"

    # Call the scrape_website function
    scraped_data = scrape_website(url)

    if scraped_data:
        print("H1 Tags:")
        print(scraped_data['h1_tags'])

        print("\nLinks:")
        print(scraped_data['links'])
