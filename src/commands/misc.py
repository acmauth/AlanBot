import discord
import configuration
import util
import asyncio
import time
from commands import Category, CommandSyntaxError, command

# Registers all the commands; takes as a parameter the decorator factory to use.
@command({
    "syntax": "test",
    "aliases": ["twoplustwo"],
    "role_requirements": {role for role in configuration.MODERATOR_ROLE},
    "category": Category.OTHER
})
async def test(message: discord.Message, parameters: str, client: discord.Client) -> None:
    """A command named 'test'"""
    result = 2 + 2
    await message.channel.send(f"Two plus two is {result}")

@command({
    "syntax": "verify <accounts>",
    "role_requirements": {role for role in configuration.MODERATOR_ROLE},
    "description": "Adds role `verified` to members."
})
async def verify(message: discord.Message, parameters: str, client: discord.Client) -> None:
    guild = client.get_guild(configuration.GUILD_ID)

    members = parameters.split(" ")
    for member in members:
        try:
            user = guild.get_member(int(member.lstrip("<@").rstrip(">")))
            await user.add_roles(guild.get_role(configuration.VERIFIED_ROLE))
            name = await guild.fetch_member(int(member.lstrip("<@").rstrip(">")))
            if not name.nick is None:
                name = name.nick
            else:
                name = name.name
            await message.channel.send(content= name + " successfully verified.")
        except:
            await message.channel.send(content="I couldn't find " + member + "! :tired_face:")
