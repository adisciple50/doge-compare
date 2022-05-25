from coinbase import *
import os
from coinbase.wallet.client import Client


class Miner:
    def __init__(self):
        self.client = Client(os.environ['coinbase_api'], os.environ['coinbase_secret'])

    def convert_to_doge(self,coin:str):
        to_doge = coin + "-doge"
        return self.client.get_buy(to_doge)

    def to_gbp(self,coin:str):
        to_gbp = coin + "-gbp"
        return self.client.get_sell(to_gbp)

    def doge_to_gbp_quote(self,doge:float):
        sell_price = self.client.get_sell_price('gbp-doge')
        return sell_price * doge # caution may produce errors!
