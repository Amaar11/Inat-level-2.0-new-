
from CoinGeckoAPIWrapper import CoinGeckoAPIWrapper
from FFETCH_TOKEN_BALANCE import TokenWallet
from VVISUALIZATIONS import PortfolioVisualizer
from PPORTFOLIO import Portfolio
from web3 import Web3, HTTPProvider
import json

# Definisanje adresa
addresses = [
    ("Contract", "0x14052a178026665BB27fd0Be549f8FB8a88780d4"),
    ("EOA", "0xC6A8109D566D31758329452c626D473B7815380E"),
    ("EOA", "0xba42C2DfbB5e876EfD9dBd198DeD5DEB2beD68C5")
]


# Lista tokena
token_ids = ["gnosis", "gelato", "cow-protocol", "usd-coin", "stakewise", "wrapped-btc-wormhole"]

# Povezivanje sa Ethereum blockchain
w3 = Web3(HTTPProvider("https://rpc.eth.gateway.fm"))

# Učitavanje konfiguracije tokena iz config.json
with open("config.json", "r") as config_file:
    tokens = json.load(config_file)["tokens"]

# Dohvaćanje i ispis trenutnih cijena za sve tokene
token_prices = CoinGeckoAPIWrapper().get_token_prices(token_ids)
print("Trenutne cijene:")
for token_id, price in token_prices.items():
    print(f"{token_id}: {price} USD " if price is not None else f"{token_id}: N/A")


# Kreiranje instance portfolija i prikazivanje salda
balance = TokenWallet(w3, addresses, tokens)
balance.display_TokenWallet_balance()


# Izračun ukupne vrijednosti portfelja
portfolio = Portfolio(w3, addresses, tokens)
total_values = portfolio.calculate_total_portfolio_value(token_prices)

# Ispis rezultata
for address, value in total_values.items():
    print(f"Address: {address}, Total Portfolio Value: {value} USD")

# Kreiranje instance PortfolioVisualizer
portfolio_visualizer = PortfolioVisualizer(total_values)

# Pozivanje metoda za kreiranje vizualizacija
portfolio_visualizer.create_token_balances_over_addresses()
portfolio_visualizer.create_token_balances_per_token()
portfolio_visualizer.create_value_in_usd_per_token(token_prices)
