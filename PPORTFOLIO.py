
from FFETCH_TOKEN_BALANCE import TokenWallet

class Portfolio:
    def __init__(self, w3, addresses, tokens):
        self.w3 = w3
        self.addresses = addresses
        self.tokens = tokens

    def calculate_total_portfolio_value(self, token_prices):
        total_values = {}
        for address_type, address in self.addresses:
            total_value = 0
            print(f"Calculating total portfolio value for {address_type}: {address}")
            # Kreiranje instance TokenWallet
            token_wallet = TokenWallet(self.w3, self.addresses, self.tokens)
            for token_name, token_address in self.tokens.items():
                # Pozivanje get_balance metode na instanci TokenWallet
                token_balance = token_wallet.get_balance(address, token_address, token_name)
                if token_balance is not None and token_name in token_prices and token_prices[token_name] is not None:
                    token_value = token_balance * token_prices[token_name]
                    total_value += token_value
                    print(f"{token_name}: {token_balance} * {token_prices[token_name]} = {token_value} USD")
            total_values[address] = total_value
            print(f"Total value for {address_type}: {total_value} USD\n")
        return total_values
