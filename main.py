if __name__ == '__main__':
    from arbitrage.database import Db
    from arbitrage.miner import Miner

    miner = Miner()
    db = Db("miner.db")
    db.create_database_if_not_exists()
    db.truncate_table()
    currencies = miner.get_all_coins()
    for coin in currencies:
        doge = miner.convert_to_doge(coin)
        coin_rate = miner.to_gbp(coin)
        doge_worth = miner.doge_to_gbp_quote(doge)
        difference = doge_worth - coin_rate
        db.insert_quote(coin_rate, doge, doge_worth, difference)
    print(db.sort_by_gbp_difference())
