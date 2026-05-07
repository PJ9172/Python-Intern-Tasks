from bs4 import BeautifulSoup
import requests
import datetime
import schedule
import csv
import time
import os

def scrape_bitcoin():

    url = "https://finance.yahoo.com/quote/BTC-INR/"
    # We MUST use headers, or Yahoo will block the script immediately
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # 2. The Hunt (Finding the price tag)
        price_tag = soup.find("span", {"data-testid": "qsp-price"})
        if price_tag:
            # Clean the string (remove commas) and convert to float
            price_text = price_tag.text.replace(",", "")
            price = float(price_text)
            
            # 3. Log the Data
            save_to_csv(price)
            print(f"Scraped Price: ₹ ${price}")
        else:
            print("Could not find the price tag. The website layout might have changed!")
        
    except Exception as e:
        print(f"Scraping Error: {e}")


def save_to_csv(price):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "timestamp" : current_time,
        "price" : price
    }

    file = "output.csv"
    file_exist = os.path.isfile(file)

    with open(file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f,fieldnames=data.keys())

        if not file_exist:
            writer.writeheader()

        writer.writerow(data)

# Automation: Run every 2 minutes
schedule.every(2).minutes.do(scrape_bitcoin)

print("Bitcoin Bot is now running... Press Ctrl+C to stop.")

# This loop keeps the script alive
while True:
    schedule.run_pending()
    time.sleep(1)