# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Function to check stock on Amazon
def check_amazon_stock(product_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Customize the selector based on the structure of the website
    stock_element = soup.find('span', {'class': 'a-declarative'})
    
    if stock_element and 'out of stock' not in stock_element.text.lower():
        return True
    else:
        return False

# Function to check stock on eBay
def check_ebay_stock(product_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Customize the selector based on the structure of the website
    stock_element = soup.find('span', {'id': 'qtySubTxt'})
    
    if stock_element and 'available' in stock_element.text.lower():
        return True
    else:
        return False

# Main function to check stock on multiple websites
def check_stock(product_url):
    amazon_stock = check_amazon_stock(product_url)
    ebay_stock = check_ebay_stock(product_url)

    print(f"Amazon: {'In Stock' if amazon_stock else 'Out of Stock'}")
    print(f"eBay: {'In Stock' if ebay_stock else 'Out of Stock'}")

# Example usage
product_url = 'https://www.amazon.com/example-product'
check_stock(product_url)
