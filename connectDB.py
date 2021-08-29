import psycopg2
import logging
import config

class ConnectDataBase():
    user = config.USER
    host = config.HOST
    database = config.DATABASE
    password = config.PASSWORD
    port = config.PORT

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
            return self.cursor().execute('select message_id from general where channel_id = 1')
        except Exception as e:
            logging.exception(e)