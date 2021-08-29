import discord
from discord.ext.commands import Bot
import logging
import os

logging.basicConfig(format = u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level = logging.INFO)

intents = discord.Intents.all()

bot = Bot(command_prefix = '/', intents = intents)


bot.load_extension('cogs.commands.send_role_embed')
bot.load_extension('cogs.event.add_role')
bot.load_extension('cogs.event.remove_role')
bot.load_extension('cogs.channel.create_channel')
bot.load_extension('cogs.commands.rules_embed')
bot.load_extension('owner_func.test')
bot.load_extension('cogs.commands.clear')


token = os.environ.get('TOKEN')
bot.run(token)