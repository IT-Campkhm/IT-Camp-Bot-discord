import logging

import pprint

import config
import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands.context import Context


class GiveRole(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):

        channel: discord.TextChannel = self.bot.get_channel(int(config.channel))
        message = await channel.fetch_message(int(config.message))
        member: discord.Member = utils.get(message.guild.members, id = payload.user_id)

        try:
            emoji = str(payload.emoji)
            role_add: discord.Role = utils.get(message.guild.roles, id = config.ROLES_ADD[emoji])

            await member.add_roles(role_add) 
        except Exception as e:
            logging.exception(repr(e))
        finally:
            logging.info(member + ' add role ' + role_add)

def setup(bot: commands.Bot):
    bot.add_cog(GiveRole(bot))
