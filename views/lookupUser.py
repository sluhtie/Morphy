import discord


class lookupUserView(discord.ui.View):

    async def lookupBTN(self, target=discord.Member):

        return discord.ui.Button(
            label='User Lookup',
            style=discord.ButtonStyle.link,
            url=f'https://discordlookup.com/user/{target.id}'
        )
