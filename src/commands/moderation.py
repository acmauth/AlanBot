from ast import literal_eval
import asyncio
import sqlite3
from time import time

import discord
import configuration
import util
from commands import Category, CommandSyntaxError, command
import logger

# Registers all the commands; takes as a parameter the decorator factory to use.


#@command({#
#    "syntax": "warn <member> | [reason]",
#    "role_requirements": {role for role in configuration.MODERATOR_ROLE},
#    "category": Category.MODERATION,
#    "description": "Warn someone"
#})
#async def warn(message: discord.Message, parameters: str, client: discord.Client, action_name="warned") -> None:
#    member_reason = await util.split_into_member_and_reason(message, parameters)
#
#    if member_reason[0] == None:
# #       raise CommandSyntaxError('You must specify a valid user.')
#
#    database_handle.cursor.execute('''INSERT INTO WARNS (ID, REASON, TIMESTAMP) \
#    VALUES(:member_id, :reason, :time)''',
#                                   {'member_id': member_reason[0].id, 'reason': str(member_reason[1]),
#                                    'time': round(time())})
#    database_handle.client.commit()
#
#    # Send a message to the channel that the command was used in
#    warn_embed = discord.Embed(title=action_name.title(),
#                               description=member_reason[0].mention) \
#        .add_field(name="Reason", value=member_reason[1])
#
#    await message.channel.send(embed=warn_embed)
