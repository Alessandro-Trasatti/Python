# In a file called bitcoin.py, implement a program that:

# Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy.
# If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
# which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions.
# Outputs the current cost of n Bitcoins in USD to four decimal places
from sys import argv, exit
import requests

link = "https://api.coindesk.com/v1/bpi/currentprice.json"
        
def search_key_in_json(data, target_key):
    if isinstance(data, dict):
        if target_key in data:
            return data[target_key]
        for key, value in data.items():
            result = search_key_in_json(value, target_key)
            if result is not None:
                return result
    elif isinstance(data, list):
        for item in data:
            result = search_key_in_json(item, target_key)
            if result is not None:
                return result
    return None

def fetch_bitcoin_price():
    try:
        response = requests.get(link)
        response.raise_for_status()
        data = response.json()
        # Dynamically search for the rate_float key
        rate = search_key_in_json(data, "rate_float")
        if rate is None:
            exit("Error: 'rate_float' not found in the JSON response.")
        return rate
    except requests.exceptions.RequestException as e:
        exit(f"Error fetching data: {e}")

def main():
    if len(argv) != 2:
        exit("Usage: python bitcoin.py <amount of bitcoin>")
    
    try:
        n_bitcoin = float(argv[1])
    except ValueError:
        exit("The command line argument should be a float representing the quantity of bitcoin.")
    
    bitcoin_USD_exchange = fetch_bitcoin_price()
    total_cost = n_bitcoin * bitcoin_USD_exchange
    print(f"Price in dollars: {total_cost:.4f}")

if __name__ == "__main__":
    main()