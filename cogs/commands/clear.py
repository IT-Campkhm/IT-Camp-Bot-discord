import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import logging

class Clear(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.command(name = 'clear')
    async def clear_message(self, ctx: Context, quantity: int = None):
        try:
            if quantity is not None:
                await ctx.channel.purge(limit = quantity + 1)
            else:
                await ctx.channel.purge(limit = 2)
        except Exception as e:
            logging.exception(e)

def setup(bot: commands.Bot):
    bot.add_cog(Clear(bot))