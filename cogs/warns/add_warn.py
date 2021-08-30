import logging

import config
import discord
import psycopg2
from discord.ext import commands
from discord.ext.commands.context import Context


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
        self.cursor = self.conn.cursor()

    @commands.command(name = 'warn')
    @commands.has_permissions(manage_guild = True)
    async def _add_warn(self, ctx: Context, member: discord.Member, reason = None):
        try:

            self.cursor.execute(f'SELECT * WHERE user_id = {member.id}')
            user = self.cursor.fetchone()

            self.conn.commit()

        except Exception as e:
            logging.exception(e)
        finally:
            if self.conn:
                self.cursor.close()
                self.conn.close()

def setup(bot: commands.Bot):
    bot.add_cog(AddWarn(bot))
