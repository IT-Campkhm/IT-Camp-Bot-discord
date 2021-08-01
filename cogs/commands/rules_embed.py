import discord
from discord import colour
from discord.ext import commands
from discord.ext.commands.context import Context
import logging


class RulesEmbed(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.command(name = 'rules_embed')
    async def _rules(self, ctx: Context):
        try:
            emb = (discord.Embed(
                title = f'Правила сервера {ctx.guild.name}',
                description = 'Вітаємо всіх в ІТ-Сamp\n'\
                    'Насамперед хочу сказати що ми дуже раді бачити нових людей в нашому колективі, людей які дійсно захоплюються ІТ сферою та хочуть вивчати щось нове',
                color = discord.Color.green() 
            )).add_field(
                name = 'Головна суть та ціль нашого буткемпа це:',
                value = '1. Мати бажання вивчати щось нове та ділитись знаннями з іншими\n'\
                        '2. Замотивувати всіх учасників ІТ-Camp\n'\
                        '3. Здійсюнвати продуктивний обмін знаннями\n'\
                        '4. Втілення ідеї учасників створюючи ІТ проекти та залучаючи до них інших(создателі можуть мати команду для утілення проекта в життя, а команда буде отрумувати стаж та вивчати щось нове)'
            ).add_field(
                name = '\u200b',
                value = 'Також, хто новий заходить на сервер змінюйте нік на ім\'я, щоб можна було легче звертатися, або ваш нік а в душках ім\'я',
                inline = False
            )

            await ctx.send(embed = emb)

        except Exception as e:
            logging.exception(e)

def setup(bot: commands.Bot):
    bot.add_cog(RulesEmbed(bot))
