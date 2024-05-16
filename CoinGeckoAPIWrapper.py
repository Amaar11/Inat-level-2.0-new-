import requests

class CoinGeckoAPIWrapper:
    def __init__(self):
        self.api_url = "https://api.coingecko.com/api/v3/simple/price"

    def get_token_prices(self, token_ids):
        params = {
            "ids": ",".join(token_ids),
            "vs_currencies": "usd"
        }
        response = requests.get(self.api_url, params=params)
        if response.status_code == 200:
            data = response.json()
            prices = {}
            for token_id in token_ids:
                if token_id in data:
                    prices[token_id] = data[token_id]["usd"]
                else:
                    prices[token_id] = None
            return prices
        else:
            print("Error:", response.status_code)
            return None
