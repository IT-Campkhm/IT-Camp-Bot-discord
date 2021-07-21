import logging
from operator import le

import config
import discord
from discord.ext import commands
from discord.utils import get


class PrivateChannel(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot
        self.all_channel = []

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        
        print(f'Before: {before}\n')
        print(f'After: {after}\n')

        '''
        category = int(config.category_id)

        if member.voice.channel is not None and member.voice.channel.id == int(config.voice_id):
            logging.info('Member connect in channel {0}'.format(after.channel.name))
            
            try:
                category_main: discord.CategoryChannel = get(member.guild.categories, id = category)
                channel: discord.VoiceChannel = await member.guild.create_voice_channel(name = f'Приватный ({member.display_name})', category = category_main)
                
                await channel.set_permissions(member, connect = True, mute_members = True, move_members = True, manage_channels = True, manage_roles = True)
                await member.move_to(channel)

                self.all_channel.append(int(channel.id))

            except Exception as e:
                logging.exception(e)
        
        if after.channel.id in self.all_channel and len(get(member.guild.voice_channel, id = after.channel.id).members) == 0:
            pass
            '''
def setup(bot: commands.Bot):
    bot.add_cog(PrivateChannel(bot))
