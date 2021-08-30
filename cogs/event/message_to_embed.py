from datetime import time
import logging

import config
import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class TransformationFromMessageToEmbed(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        try:
            await self.bot.process_commands(message)
            
            if message.channel.id == 881678339356622898 and not message.embeds:
                
                text = message.content
                msg: discord.Message = await message.channel.fetch_message(message.id)

                emb = (discord.Embed(
                    description = f'{text}',
                    timestamp = message.created_at,
                    color = discord.Color.from_rgb(255, 255, 255)
                ))
                
                await msg.delete()
                await message.channel.send(embed = emb)

        except Exception as e:
            logging.exception(e)

def setup(bot: commands.Bot):
    bot.add_cog(TransformationFromMessageToEmbed(bot))