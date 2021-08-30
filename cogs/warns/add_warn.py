import logging

import config
import discord
import psycopg2
from discord.ext import commands
from discord.ext.commands.context import Context


class AddWarn(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name = 'warn')
    @commands.has_permissions(manage_guild = True)
    async def _add_warn(self, ctx: Context, member: discord.Member, reason = None):
        try:
            pass
        except Exception as e:
            logging.exception(e)

def setup(bot: commands.Bot):
    bot.add_cog(AddWarn(bot))
