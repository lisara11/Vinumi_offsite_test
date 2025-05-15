import requests
from bs4 import BeautifulSoup

def fetch_stock_price():
    # Define the target URL
    url = "https://finance.yahoo.com/quote/AAPL?p=AAPL"
    # Set headers to simulate a real browser
    headers={"User-Agent": "Mozilla/5.0"}
    # Send a GET request
    response= requests.get(url,headers=headers)

    # Check if the request was successful
    if response.status_code !=200:
        print("Failed to get data. status code:", response.status_code)
        return
    # Parse the HTML content
    soup=BeautifulSoup(response.text, "html.parser")

    # Find the stock price element
    try:
        price_element= soup.find("fin-streamer",{"data-field": "regularMarketPrice"})
        price_text= price_element.text.strip()
        stock_price= float(price_text.replace(',',''))

        print(f"Apple stock price: ${stock_price}")
        return stock_price
    except Exception as e:
        print("stock price not found. error:", e)

# Run the function
fetch_stock_price()