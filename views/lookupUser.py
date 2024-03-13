import discord
from discord.ui import Button


class lookupUserBTN(discord.ui.View):

    async def button(self, label='User Lookup', style=discord.ButtonStyle.link, url=None):
        return discord.ui.Button(label=label, style=style, url=url)

