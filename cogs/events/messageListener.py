import discord
from discord.ext import commands

import config


class MessageListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener
    async def on_message_delete(self, message: discord.Message):
        if message.author != self.bot.user:
            await message.author.guild.get_channel(config.MESSAGE_LOGS).send(embed=message_log_embed(before=message))

    @commands.Cog.listener
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        if before.author != self.bot.user:
            await before.author.guild.get_channel(config.MESSAGE_LOGS).send(embed=message_log_embed(before, after))


def message_log_embed(before: discord.Message = None, after: discord.Message = None):

    if after is not None:
        title = "Message Edited"
        color = discord.Colour.from_rgb(230, 196, 75)
        timestamp = after.created_at
    else:
        title = "Message Deleted"
        color = discord.Colour.from_rgb(230, 78, 75)
        timestamp = before.created_at

    embed = discord.Embed(
        title=title,
        color=color,
        timestamp=timestamp
    )

    embed.add_field(name='Author', value=before.author.mention, inline=True)
    embed.add_field(name='Channel', value=before.channel.mention, inline=True)

    if after is not None:
        msg_link = f"https://discord.com/channels/{before.guild.id}/{before.channel.id}/{before.id}"
        embed.add_field(name='Message Reference', value=msg_link, inline=True)
        embed.add_field(name='Original Message', value=f"```{before.content}```", inline=False)
        embed.add_field(name='Edited Message', value=f"```{after.content}```", inline=False)
        embed.set_thumbnail(url='https://i.imgur.com/0bsXJlw.png')
    else:
        embed.add_field(name='Message ID', value=f"`{before.id}`", inline=True)
        embed.add_field(name='Message', value=f"```{before.content}```", inline=False)
        embed.set_thumbnail(url='https://i.imgur.com/zWiY6Dr.png')

    embed.set_footer(icon_url=before.author.avatar.url)
    return embed


def setup(bot): bot.add_cog(MessageListener(bot))
