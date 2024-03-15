import discord
from discord.ext import commands
import views.lookupUser


class UserInfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name='userinfo', description='Provides information about a Discord Member')
    async def get_user_info_cmd(self, ctx, member: discord.Option(discord.Member) = None):
        target = member if member else ctx.author
        view = views.lookupUser.lookupUserBTN()
        view.add_item(await views.lookupUser.button(url=f'https://discordlookup.com/user/{target.id}'))
        await ctx.respond(embed=await get_user_info_embed(bots=self.bot, member=target), view=view, ephemeral=True)


async def get_user_info_embed(bots: discord.Bot, member: discord.Member):
    embed = discord.Embed(
        title='User Information:',
        color=discord.Color.from_rgb(100, 255, 100)
    )

    embed.add_field(name='Username', value=f"```{member}```", inline=True)
    embed.add_field(name='Discord ID', value=f'```{member.id}```', inline=True)
    embed.add_field(name='', value='', inline=True)

    embed.add_field(name='Creation Date:', value=f'<t:{member.created_at.timestamp().__floor__()}:f>', inline=True)
    embed.add_field(name='Join Date:', value=f'<t:{member.joined_at.timestamp().__floor__()}:f>', inline=True)
    embed.add_field(name='', value='', inline=True)

    roles = ", ".join(str(role.mention) for role in reversed(member.roles) if role.name != '@everyone')
    embed.add_field(name='Roles:', value=f'{roles}', inline=False)

    embed.set_thumbnail(url=member.avatar.url)

    # user = await bots.fetch_user(member.id)
    # embed.set_image(url=user.banner.url)
    return embed


def setup(bot):
    bot.add_cog(UserInfo(bot))
