import sqlite3


class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()



    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()
