from web3 import Web3, HTTPProvider
from web3.exceptions import ABIFunctionNotFound
import json

class TokenWallet:
    def __init__(self, w3, addresses, tokens):
        self.w3 = w3
        self.addresses = addresses
        self.tokens = tokens

    def get_balance(self, address, token_address, token_name):
        try:
            abi_filename = f"abi/{token_address}_abi.json"
            with open(abi_filename, "r") as abi_file:
                token_abi = json.load(abi_file)

            token_contract = self.w3.eth.contract(address=token_address, abi=token_abi)
            token_balance = token_contract.functions.balanceOf(address).call()
            decimals = token_contract.functions.decimals().call()
            token_balance_adjusted = token_balance / (10 ** decimals)

            return token_balance_adjusted
        except ABIFunctionNotFound:
            print(f"ERROR: Function 'balanceOf' not found for token {token_name}")
        except FileNotFoundError:
            print(f"ERROR: ABI file not found for token {token_name}")

    def display_TokenWallet_balance(self):
        for address_type, address in self.addresses:
            print(f"Balance for {address_type}: {address}")
            for token_name, token_address in self.tokens.items():
                token_balance = self.get_balance(address, token_address, token_name)
                if token_balance is not None:
                    print(f"{token_name}: {token_balance}")
            print()


