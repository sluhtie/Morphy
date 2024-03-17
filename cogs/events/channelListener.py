import datetime

import discord
from discord.ext import commands

import config


class ChannelListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState,
                                    after: discord.VoiceState):
        if before.channel != after.channel:

            if before.channel is None:
                title = 'Voice channel joined'
                color = discord.Color.from_rgb(134, 227, 100)
            elif after.channel is None:
                title = 'Voice channel left'
                color = discord.Color.from_rgb(245, 81, 66)
            else:
                title = 'Voice channel switched'
                color = discord.Color.from_rgb(66, 135, 245)

            embed = discord.Embed(
                color=color,
                timestamp=datetime.datetime.now()
            )

            embed.add_field(name='Member', value=member.mention, inline=True)
            embed.add_field(name='Member ID', value=f'`{member.id}`', inline=True)
            if before.channel is None and after.channel is not None:
                embed.add_field(name='', value=f'User has joined channel {after.channel.mention}', inline=False)
            elif after.channel is None and before.channel is not None:
                embed.add_field(name='', value=f'User has left channel {before.channel.mention}', inline=False)
            elif after.channel is not None and before.channel is not None:
                embed.add_field(name='',
                                value=f'User has switched from {before.channel.mention} to {after.channel.mention}',
                                inline=False)

            embed.set_author(name=title, icon_url='https://cdn-icons-png.freepik.com/512/8334/8334028.png')
            await member.guild.get_channel(config.VOICE_LOGS).send(embed=embed)


def setup(bot): bot.add_cog(ChannelListener(bot))
