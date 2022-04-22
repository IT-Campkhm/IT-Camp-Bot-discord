import discord
from discord.ext import commands
import logging
from config import CHANNEL_RULES, CHANNEL_GREETING, CNANNEL_ROLES

class MemberJoinedGuild(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        try:

            channel_rules = self.bot.get_channel(CHANNEL_RULES)
            channel_greeting = await member.create_dm()
            cnannel_roles = self.bot.get_channel(CNANNEL_ROLES)

            emb = (discord.Embed(
               title = f'Вітаємо тебе на сервері спільноти {ctx.guild.name}!\n\n',
                description ='• Головна мета IT-camp це зробити комфортне місце для вивчення різних напрямів ІТ-технологій в професійному середовищі з неймовірною атмосферою та крутою командою💥\n\n' \
                            f'• Вибери професію та напрями, які ти вивчаєш в каналі  {channel_rules.mention} \n'
                            f'• Також можете вибрати роль в каналі {cnannel_roles.mention}, яка найбільше підходить до вашого виду діяльності \n'
                            f'• Зміни нік на ім`я щоб можна було зрозуміти як звертатись \n'
                            f'• Пройди коротку анкету учасника https://forms.gle/JtXAXBG5fhvJRDuv5 \n\n'
                            f' А тепер...ласкаво просимо до команди🤘🏻 ',
                timestamp = ctx.message.created_at
            )#.set_footer(
              #  text = f'{ctx.author.id} | Приємно провести час на нашому проекті',
              #  icon_url = ctx.author.avatar_url
          #  )
            )
            await channel_greeting.send(f'{member.mention}', embed = emb)

        except Exception as e:
            logging.exception(e)

def setup(bot: commands.Bot):
    bot.add_cog(MemberJoinedGuild(bot))