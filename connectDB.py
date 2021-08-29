import psycopg2
import logging
import config

class ConnectDataBase():
    def __init__(self) -> None:
        self.user = config.USER
        self.host = config.HOST
        self.database = config.DATABASE
        self.password = config.PASSWORD
        self.port = config.PORT

    def cursor(self):
        try:
            
            conn = psycopg2.connect(
                user = self.user,
                host = self.host,
                database = self.database,
                password = self.password,
                port = self.port
            )

            return conn.cursor()

        except Exception as e:
            logging.exception(e)

    def select(self):
        try:
            self.cursor().execute('select message_id from general where channel_id = 1')
            print(self.cursor().fetchall())
            
            return self.cursor().execute('select message_id from general where channel_id = 1')
        except Exception as e:
            logging.exception(e)