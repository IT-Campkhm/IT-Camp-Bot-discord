import logging

import config
import discord
import psycopg2
from discord.ext import commands
from discord.ext.commands.context import Context


class TestOwner(commands.Cog):
    username = config.USER
    host = config.HOST
    database = config.DATABASE
    password = config.PASSWORD
    port = 5432

    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.command(name = 'test')
    @commands.is_owner()
    async def _test_owner(self, ctx: Context):
        try:
            conn = psycopg2.connect(
                user = self.username,
                host = self.host,
                database = self.database,
                password = self.password,
                port = self.port
            )

            cursor = conn.cursor()
            
            cursor.execute("SELECT message_id FROM public.general WHERE channel_id = 1")
            data = cursor.fetchone()
            conn.commit()

            await ctx.send(f'{data[0][0]}\n{data[0][1]}')
        except Exception as e:
            logging.exception(e)

def setup(bot: commands.Bot):
    bot.add_cog(TestOwner(bot))
