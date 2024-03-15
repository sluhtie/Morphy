import discord
from discord.ui import Button


async def button(label='User Lookup', style=discord.ButtonStyle.link, url=None):
    return discord.ui.Button(label=label, style=style, url=url)


class lookupUserBTN(discord.ui.View):
    pass

