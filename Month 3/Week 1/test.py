import requests
from bs4 import BeautifulSoup

def scrape_bitcoin():
    url = "https://finance.yahoo.com/quote/BTC-INR"
    
    # Expanded headers to bypass the "No Title" block
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }

    try:
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}") # Check for 200

        soup = BeautifulSoup(response.text, "html.parser")
        
        # Method 1: The data-testid you found
        price_tag = soup.find("span", {"data-testid": "qsp-price"})
        
        # Method 2: Fallback to fin-streamer if span fails
        if not price_tag:
            price_tag = soup.find("fin-streamer", {"data-field": "regularMarketPrice"})

        if price_tag:
            price = price_tag.text
            print(f"Success! Bitcoin Price: {price}")
        else:
            # This will tell us if we are looking at a "Request Denied" page
            print(f"Failed to find tag. Title of page received: {soup.title.string if soup.title else 'Still No Title'}")
            
    except Exception as e:
        print(f"Error: {e}")

scrape_bitcoin()