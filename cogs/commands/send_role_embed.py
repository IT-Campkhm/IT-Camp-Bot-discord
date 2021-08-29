import asyncio
import logging
import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import config
import psycopg2


class RemoveRole(commands.Cog):
    username = config.USER
    host = config.HOST
    database = config.DATABASE
    password = config.PASSWORD
    port = 5432

    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot
        self.conn = psycopg2.connect(
            user = self.username,
            host = self.host,
            database = self.database,
            password = self.password,
            port = self.port
        )

    @commands.command(name = 'send_role_embed')
    @commands.has_permissions(administrator = True)
    async def _send_role_embed(self, ctx: Context):
        try:
            
            emb_1 = (discord.Embed(
                title = 'Виберіть роль',
                description = '🖥️ - Верстальщик\n'\
                    '🕸️ - Бекенд\n'\
                    '<:gamedev:866780079370665994> - Ігродел\n'\
                    '🌳 - 3Д модельер\n'\
                    '🛠️ - Soft Develompent\n'\
                    '🤖 - Arduino',
                    colour = discord.Color.green()
            ))

            emb_2 = (discord.Embed(
                description = '<a:cpp:866776827762442240> - C++\n'\
                    '<a:csharp:866777010294226964> - C#\n'\
                    '<a:python:866776924147286027> - Python\n'\
                    '<a:javascript:866777189889343540> - JavaScript\n'\
                    '<:java:866781829495652403> - Java\n'\
                    '<a:sql:866777146273038387> - SQL',
                    colour = discord.Color.green()
            ))

            emb_3 = (discord.Embed(
                description = '<a:blender:866784801838989392> - Blender\n'\
                    '🎨 - 3Dmax\n'\
                    '🎛️ - Unity\n'\
                    '⚙️ - UnrealEngine\n'\
                    '🛡️ - HTML\CSS\n'\
                    '<a:php:866777065688924170> - PHP\n'\
                    '<a:rubby:866776968023244800> - Rubby',
                    colour = discord.Color.green()
            ))

            await ctx.channel.purge(limit = 1)
            message_1: discord.Message = await ctx.send(embed = emb_1)
            message_2: discord.Message = await ctx.send(embed = emb_2)
            message_3: discord.Message = await ctx.send(embed = emb_3)
            
            print(message_1.id)
            print(message_2.id)
            print(message_3.id)

            cursor = self.conn.cursor()
            cursor.execute(f'INSERT INTO public.general(channel_id, message_id) VALUES ({ctx.channel.id}, array[{message_1.id}, {message_2.id}, {message_3.id}]);')
            self.conn.commit()

            for one_emb in range(0, 6):
                await message_1.add_reaction(config.r[one_emb])
                await asyncio.sleep(1)
            
            for two_emb in range(6, 12):
                await message_2.add_reaction(config.r[two_emb])
                await asyncio.sleep(1)
            
            for three_emb in range(12, 18):
                await message_3.add_reaction(config.r[three_emb])
                await asyncio.sleep(1)
            
        except Exception as e:
            logging.info(e)

def setup(bot: commands.Bot):
    bot.add_cog(RemoveRole(bot))