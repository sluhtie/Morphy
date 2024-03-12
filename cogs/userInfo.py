import discord
from discord.ext import commands


class UserInfo(commands.Cog):

    def __init__(self, bot):  # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(name='userinfo', description='Provides information about a Discord Member')  # we can also add application commands
    async def get_user_info_cmd(self, ctx, member: discord.Option(discord.Member) = None):
        if member:
            await ctx.respond(embed=get_user_info(member))
        else:
            await ctx.respond(embed=get_user_info(ctx.author))


    @discord.user_command(name='Get User Info')
    async def get_user_info_ctx(self, ctx, member: discord.Member):
        await ctx.respond(embed=get_user_info(member))


def get_user_info(member: discord.Member):
    embed = discord.Embed(
        title='Hello',
        description=f'UserInfo: {member.name} ({member.id})',
        color=discord.Color.from_rgb(100, 133, 100)
    )
    embed.add_field(name='Discord ID', value=f'```{member.id}```', inline=True)
    embed.add_field(name='Username', value=member, inline=True)
    return embed


def setup(bot):
    bot.add_cog(UserInfo(bot))
