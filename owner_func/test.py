import logging

import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from config import CHANNEL_RULES, CHANNEL_GREETING, CNANNEL_ROLES

class TestOwner(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot
        self.channel_rules = self.bot.get_channel(CHANNEL_RULES)
        self.channel_greeting = self.bot.get_channel(CHANNEL_GREETING)
        self.cnannel_roles = self.bot.get_channel(CNANNEL_ROLES)

    @commands.command(name = 'test')
    @commands.is_owner()
    async def _test_owner(self, ctx: Context):
        try:
            emb = (discord.Embed(
                title = f'Вітаємо вас на сервері проекту {ctx.guild.name}!',
                description = 'Головна мета IT-camp це зробити комфортне місце для вивчення різних напрямів ІТ-технологій в професійному середовищі з неймовірною атмосферою та крутою командою💥\n' \
                            f'Ознайометесь з правилами проекту в каналі {self.channel_rules.mention}.\n'
                            f'Також можете вибрати роль в каналі {self.cnannel_roles.mention}, яка найбільше підходить до вашого виду діяльності.',
                timestamp = ctx.message.created_at
            ).set_footer(
                text = f'{ctx.author.id} | Приємно провести час на нашому проекті',
                icon_url = ctx.author.icon_url
            ))
            await self.channel_greeting.send(f'{ctx.author.mention}', embed = emb)
        except Exception as e:
            logging.exception(e)

def setup(bot: commands.Bot):
    bot.add_cog(TestOwner(bot))
