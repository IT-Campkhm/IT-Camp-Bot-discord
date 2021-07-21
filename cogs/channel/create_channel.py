import logging

import config
import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.utils import get


class PrivateChannel(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        
        print(f'\n{member}\n\n{before}\n\n{after}\n')

        if member.voice.channel.id == int(config.voice_id) and after.channel is not None:
            logging.info('Member connect in channel {0}'.format(after.channel.name))
        
        '''
        try:
            if after.channel is not None and member.voice.channel.id == int(config.voice_id)

        except Exception as e:
            logging.exception(e)
        '''

def setup(bot: commands.Bot):
    bot.add_cog(PrivateChannel(bot))
