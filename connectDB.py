import psycopg2
import logging
import config

class ConnectDataBase():
    username = config.USER
    host = config.HOST
    database = config.DATABASE
    password = config.PASSWORD
    port = 5432

    def cursor(self):
        try:
            
            conn = psycopg2.connect(
                user = self.username,
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
            self.cursor().execute('SELECT message_id FROM public.general WHERE channel_id = 1;')
            print(self.cursor().fetchall())
            
            return self.cursor().execute('SELECT message_id FROM public.general WHERE channel_id = 1;')
        except Exception as e:
            logging.exception(e)