from coinbase import *
import os
from coinbase.wallet.client import Client
from arbitrage.credentials import AuthManager


class Miner:
    def __init__(self):
        credentials = AuthManager().authenticate()
        self.client = Client(credentials["api"], credentials["secret"])

    def get_all_coins(self):
        fiat = self.client.get_currencies()
        fiat_ids = []
        for item in list(fiat["data"]):
            fiat_ids += [item["id"]]
        coins = self.client.get_exchange_rates(currency='GBP').rates.keys()

        return fiat_ids + list(coins)



    def convert_to_doge(self, coin: str):
        to_doge = coin + "-doge"
        return self.client.get_spot_price(currencey_pair= to_doge).amount

    def to_gbp(self, coin: str):
        to_gbp = coin + "-gbp"
        return self.client.get_sell_price(currencey_pair= to_gbp).amount

    def doge_to_gbp_quote(self, doge: float):
        sell_price = self.client.get_sell_price(currency_pair= 'DOGE-GBP').amount
        print(sell_price)
        print(doge)
        return float(sell_price) * float(doge)  # caution may produce errors!
