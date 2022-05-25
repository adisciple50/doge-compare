import sqlite3


class Db:
    def __init__(self, database: str = 'test'):
        self.con = sqlite3.connect(database)  # database

    def create_database_if_not_exists(self):
        self.con.execute("CREATE TABLE [IF NOT EXISTS] [main].quotes (coin_to_gbp float NOT NULL,coin_to_doge_exchange_rate float NOT NULL,exchanged_doge_worth_in_gbp float NOT NULL,gbp_difference float NOT NULL) [ WITHOUT ROWID];")
        self.con.commit()

    # coin is the coin to convert to doge and
    def insert_quote(self,coin_to_gbp:float,coin_to_doge_exchange_rate:float,exchanged_doge_worth_in_gbp:float,gbp_difference:float):
        self.con.execute("INSERT INTO quotes(coin_to_gbp,coin_to_doge_exchange_rate,exchanged_doge_worth_in_gbp,gbp_difference) VALUES(coin_to_gbp,coin_to_doge_exchange_rate,exchanged_doge_worth_in_gbp,gbp_difference")
        self.con.commit()

    def sort_by_gbp_difference(self):
        self.con.execute("SELECT * FROM quotes ORDER BY gbp_difference")
        self.con.commit()

    def truncate_table(self):
        self.con.execute("DELETE FROM quotes")
        self.con.commit()
