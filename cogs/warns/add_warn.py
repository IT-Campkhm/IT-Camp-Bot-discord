import logging

import config
import discord
import psycopg2
from discord.ext import commands
from discord.ext.commands.context import Context
import datetime


class AddWarn(commands.Cog):
    username = config.USER
    host = config.HOST
    database = config.DATABASE
    password = config.PASSWORD
    port = 5432

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.conn = psycopg2.connect(
            user = self.username,
            host = self.host,
            database = self.database,
            password = self.password,
            port = self.port
        )

    @commands.command(name = 'warn')
    @commands.has_permissions(manage_guild = True)
    async def _add_warn(self, ctx: Context, member: discord.Member, reason = None):
        try:

            cursor = self.conn.cursor()

            cursor.execute(f'SELECT user_id, quantati, where_add, who_add_warn FROM public.user_warns WHERE user_id = {member.id};')
            user = cursor.fetchone()
            self.conn.commit()

            logging.info(user)

            if user is not None:
                
                cursor.execute(f'SELECT quantati FROM public.user_warns WHERE user_id = {member.id};')
                quantati = cursor.fetchone()
                self.conn.commit()

                cursor.execute(f'SELECT who_add_warn FROM public.user_warns WHERE user_id = {member.id};')
                who_add_warn = cursor.fetchone()
                self.conn.commit()

                cursor.execute(f'SELECT where_add FROM public.user_warns WHERE user_id = {member.id}')
                where_add = cursor.fetchone()
                self.conn.commit()

                logging.info(quantati)
                logging.info(who_add_warn)
                logging.info(where_add)
                '''
                self.cursor.execute(
                    'UPDATE public.user_warns SET quantati=?, where_add=?, who_add_warn=? WHERE <condition>;'
                )
                '''
            
            else:

                self.cursor.execute(
                    f'INSERT INTO public.user_warns(user_id, quantati, where_add, who_add_warn) VALUES ({member.id}, {1}, \{\'{datetime.date.today()}\'\}, array[{ctx.author.id}]);'
                )

        except Exception as e:
            logging.exception(e)
        
        finally:
            if self.conn:
                self.cursor.close()
                self.conn.close()

def setup(bot: commands.Bot):
    bot.add_cog(AddWarn(bot))
