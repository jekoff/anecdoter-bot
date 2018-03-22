import sqlite3
import os
import config


class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_random_joke(self):
        query = "SELECT * FROM aneks WHERE id IN (SELECT id FROM aneks ORDER BY RANDOM() LIMIT 1)"
        with self.connection:
            return self.cursor.execute(query).fetchone()[2]

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()


