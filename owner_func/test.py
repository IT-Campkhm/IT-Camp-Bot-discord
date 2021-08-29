import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import logging
from connectDB import ConnectDataBase

class TestOwner(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot
        #self.bd = ConnectDataBase()

    @commands.command(name = 'test')
    @commands.is_owner()
    async def _test_owner(self, ctx: Context):
        try:
            await ctx.send(f'{ConnectDataBase().select()}')
        except Exception as e:
            logging.exception(e)

def setup(bot: commands.Bot):
    bot.add_cog(TestOwner(bot))