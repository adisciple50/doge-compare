if __name__ == '__main__':
    from arbitrage.database import Db
    from arbitrage.miner import Miner

    miner = Miner()
    db = Db("miner.db")
    db.create_database_if_not_exists()
    db.truncate_table()
    currencies = miner.get_all_coins()
    print(currencies)
    for coin in currencies:
        doge = miner.convert_to_doge(coin)
        coin_rate = miner.to_gbp(coin)
        doge_worth = miner.doge_to_gbp_quote(doge)
        profit = float(doge_worth) - float(coin_rate)
        db.insert_quote(coin, coin_rate, doge, doge_worth, profit)
    print(db.sort_by_gbp_difference())
# doge is not the amount bought by the pair currency