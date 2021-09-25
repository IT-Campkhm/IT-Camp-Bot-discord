import discord
from discord.ext import commands
import logging
from config import OWNER


class BotOnReady(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            owner: discord.Member = self.bot.get_user(OWNER)
            await owner.send(
                'Бот запустився\n'\
                f'Bot ID: {self.bot.user.id}\n'\
                f'Bot Name: {self.bot.user.name}\n'\
                f'Bot Owner ID: {self.bot.owner_id}'
            )
        except Exception as e:
            logging.exception(e)

def setup(bot: commands.Bot):
    bot.add_cog(BotOnReady)