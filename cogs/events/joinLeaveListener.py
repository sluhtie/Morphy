import discord
from discord.ext import commands

import config


class JoinLeaveListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        guild = member.guild
        join_log_channel = config.LOG_CHANNEL
        welcome_channel = config.WELCOME_CHANNEL

        await welcome_channel.send(f"Welcome {member.mention} to {guild.name}!")
        await join_log_channel.send(embed=join_log_embed(member))

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        join_log_channel = member.guild.get_channel(config.LOG_CHANNEL)
        await join_log_channel.send(embed=leave_log_embed(member))


# Join Log Embed
def join_log_embed(member):
    embed = discord.Embed(
        title=f"New member",
        description=f'User {member.mention} has joined the Server (#{member.guild.member_count})',
        color=discord.Color.from_rgb(50, 200, 50)
    )
    embed.set_thumbnail(url=member.avatar.url)
    embed.add_field(name="Created", value=f'<t:{member.created_at.timestamp().__floor__()}:f>', inline=True)
    embed.add_field(name='ID', value=f"`{member.id}`", inline=True)
    return embed


# Leave Log Embed
def leave_log_embed(member):
    embed = discord.Embed(
        title=f"Member Left",
        description=f'Member {member.mention} has left the Server! (#{member.guild.member_count})',
        color=discord.Color.from_rgb(200, 50, 50)
    )
    embed.set_thumbnail(url=member.avatar.url)
    embed.add_field(name="Joined", value=f'<t:{member.joined_at.timestamp().__floor__()}:f>', inline=True)
    embed.add_field(name='ID', value=f"`{member.id}`", inline=True)
    return embed


def setup(bot): bot.add_cog(JoinLeaveListener(bot))
