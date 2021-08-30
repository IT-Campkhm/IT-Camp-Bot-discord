import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import logging

class SendEmbedBot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.command(name = 'send_embed')
    async def _send_message_embed_use_bot(self, ctx: Context, *, text):
        try:
            emb = (discord.Embed(
                description = f'{text}',
                timestamp = ctx.message.create_at
            ))

            await ctx.send(embed = emb)
        except Exception as e:
            logging.exception(e)

def setup(bot: commands.Bot):
    bot.add_cog(SendEmbedBot(bot))