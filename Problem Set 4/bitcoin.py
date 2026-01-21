# takes in the numbr of bitcoins that they would like to buy, n
# queries the API for CoinCap Bitcoin Price Index
# outputs the current cost of n bitcoins in USD to 4 decimal places


import requests
import sys

api_key = "ENTER YOUR API KEY" # replace with your own api


def get_value(num): # gets the value of one biction and returns that times the number the user selected
    try:
        response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}")
    except requests.RequestException:
        sys.exit("Bad Request")
    data = response.json()
    return float(data["data"]["priceUsd"]) * num


def main():
    args = sys.argv
    try:
        num = float(args[1])    
    except ValueError:
        sys.exit("Value Error")

    print(f"${get_value(num):,.4f}")

    

if __name__ == "__main__":
    main()