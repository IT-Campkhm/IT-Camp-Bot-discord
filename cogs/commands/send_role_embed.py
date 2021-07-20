import logging
import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands.context import Context
import config


class RemoveRole(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name = 'send_role_embed')
    async def _send_role_embed(self, ctx: Context):
        emb = (discord.Embed(
            title = 'Виберіть роль',
            description = '🖥️ - Верстальщик\n'\
                '🕸️ - Бекенд\n'\
                '<:gamedev:866780079370665994> - Ігродел\n'\
                '🌳 - 3Д модельер\n'\
                '🛠️ - Soft Develompent\n'\
                '🤖 - Arduino\n'\
                '<a:cpp:866776827762442240> - C++\n'\
                '<a:csharp:866777010294226964> - C#\n'\
                '<a:python:866776924147286027> - Python\n'\
                '<a:javascript:866777189889343540> - JavaScript\n'\
                '<:java:866781829495652403> - Java\n'\
                '<a:sql:866777146273038387> - SQL\n'\
                '<a:blender:866784801838989392> - Blender\n'\
                '🎨 - 3Dmax\n'\
                '🎛️ - Unity\n'\
                '⚙️ - UnrealEngine\n'\
                '🛡️ - HTML\CSS\n'\
                '<a:php:866777065688924170> - PHP\n'\
                '<a:rubby:866776968023244800> - Rubby\n',
                colour = discord.Color.green()
        ))

        await ctx.channel.purge(limit = 1)
        message = await ctx.send(embed = emb)
        
        for i in range(len(config.r)):
            await message.add_reaction(config.r[i])

def setup(bot: commands.Bot):
    bot.add_cog(RemoveRole(bot))