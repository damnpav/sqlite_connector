import sqlite3
import pandas as pd


class SqliteConnector:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)

    def get_data(self, query_str):
        """
        Extract data from db into Pandas object
        :param query_str: string with sql query
        :return: Pandas DataFrame with result table
        """
        return pd.read_sql_query(query_str, self.conn)

    def execute_query(self, query_str):
        """
        Execute query at database
        :param query_str: sql query
        :return:
        """
        cursor = self.conn.cursor()
        cursor.execute(query_str)
        self.conn.commit()
        return f'Result: {cursor.fetchall()}'


