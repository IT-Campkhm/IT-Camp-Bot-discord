import logging

import config
import discord
import psycopg2
from discord import utils
from discord.ext import commands

class GiveRole(commands.Cog):
    username = config.USER
    host = config.HOST
    database = config.DATABASE
    password = config.PASSWORD
    port = 5432

    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot
        self.conn = psycopg2.connect(
            user = self.username,
            host = self.host,
            database = self.database,
            password = self.password,
            port = self.port
        )

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent): # Перше повідомлення з вибором ролі

        if not payload.member.bot:

            cursor = self.conn.cursor()

            cursor.execute(f'SELECT message_id FROM public."general" WHERE channel_id = {payload.channel_id};')
            channel_id = cursor.fetchone()
            self.conn.commit()
            logging.info(channel_id)

            channel: discord.TextChannel = self.bot.get_channel(payload.channel_id)
            message = await channel.fetch_message(channel_id[0][0])
            member: discord.Member = utils.get(message.guild.members, id = payload.user_id)

            try:
                emoji = str(payload.emoji)
                role_add: discord.Role = utils.get(message.guild.roles, id = config.ROLES_ADD[emoji])

                await member.add_roles(role_add) 
            except Exception as e:
                logging.exception(repr(e))
            finally:
                logging.info(f'{member}' + ' add role ' + f'{role_add.name}')
                if self.conn:
                    self.cursor.close()
                    self.conn.close()
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent): # Друге повідомлення з вибором ролі

        if not payload.member.bot:

            cursor = self.conn.cursor()

            cursor.execute(f'SELECT message_id FROM public."general" WHERE channel_id = {payload.channel_id};')
            channel_id = cursor.fetchone()
            self.conn.commit()
            logging.info(channel_id)

            channel: discord.TextChannel = self.bot.get_channel(payload.channel_id)
            message = await channel.fetch_message(channel_id[0][1])
            member: discord.Member = utils.get(message.guild.members, id = payload.user_id)

            try:
                emoji = str(payload.emoji)
                role_add: discord.Role = utils.get(message.guild.roles, id = config.ROLES_ADD[emoji])

                await member.add_roles(role_add) 
            except Exception as e:
                logging.exception(repr(e))
            finally:
                logging.info(f'{member}' + ' add role ' + f'{role_add.name}')
                if self.conn:
                    self.cursor.close()
                    self.conn.close()
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent): # Третє повідомлення з вибором ролі

        if not payload.member.bot:

            cursor = self.conn.cursor()

            cursor.execute(f'SELECT message_id FROM public."general" WHERE channel_id = {payload.channel_id};')
            channel_id = cursor.fetchone()
            self.conn.commit()
            logging.info(channel_id)

            channel: discord.TextChannel = self.bot.get_channel(payload.channel_id)
            message = await channel.fetch_message(channel_id[0][2])
            member: discord.Member = utils.get(message.guild.members, id = payload.user_id)

            try:
                emoji = str(payload.emoji)
                role_add: discord.Role = utils.get(message.guild.roles, id = config.ROLES_ADD[emoji])

                await member.add_roles(role_add) 
            except Exception as e:
                logging.exception(repr(e))
            finally:
                logging.info(f'{member}' + ' add role ' + f'{role_add.name}')
                if self.conn:
                    self.cursor.close()
                    self.conn.close()

def setup(bot: commands.Bot):
    bot.add_cog(GiveRole(bot))
    print(bot)
