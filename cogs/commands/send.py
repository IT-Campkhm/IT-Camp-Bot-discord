import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import logging

class SendBot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.command(name = 'send')
    @commands.has_permissions(manage_guild = True)
    async def _send_message_use_bot(self, ctx: Context, *, text):
        try:
            await ctx.channel.purge(limit = 1)
            await ctx.send(f'{text}')
        except Exception as e:
            logging

def setup(bot: commands.Bot):
    bot.add_cog(SendBot(bot))