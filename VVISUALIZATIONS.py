import matplotlib.pyplot as plt

class PortfolioVisualizer:
    def __init__(self, total_values):
        self.total_values = total_values

    def create_token_balances_over_addresses(self):
        plt.figure(figsize=(10, 6))
        for address_type, address_values in self.total_values.items():
            plt.plot(address_values, label=address_type)
        plt.title('Token Balances Over Addresses')
        plt.xlabel('Token')
        plt.ylabel('Balance')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()


    def create_token_balances_per_token(self):
        tokens = list(self.total_values.keys())
        values = list(self.total_values.values())
        values_flat = []

        for sublist in values:
            if isinstance(sublist, int):
                values_flat.append([sublist])
            else:
                values_flat.append(sublist)

        values_flat = [item for sublist in values_flat for item in sublist]


        plt.figure(figsize=(10, 6))
        plt.bar(tokens, values_flat, color='skyblue')
        plt.title('Token Balances Per Token')
        plt.xlabel('Token')
        plt.ylabel('Balance')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


    def create_value_in_usd_per_token(self, token_prices):
        tokens = list(self.total_values.keys())
        values = list(self.total_values.values())

        plt.figure(figsize=(10, 6))

        # Provjeri da li svaki token postoji u token_prices
        for i, token in enumerate(tokens):
            if token in token_prices:
                # Izračunaj vrijednost u USD po tokenu
                value_usd = [balance * token_prices[token] for balance in values[i]]

                # Prikaži vrijednost u USD po tokenu
                plt.bar(range(len(value_usd)), value_usd, label=token)
            else:
                print(f"Token '{token}' nije pronađen u cijenama tokena. Preskačem...")

        handles, labels = plt.gca().get_legend_handles_labels()
        if handles:
            plt.legend()

        plt.title('Value in USD Per Token')
        plt.xlabel('Token Balance Index')
        plt.ylabel('Value in USD')
        plt.tight_layout()
        plt.show()


