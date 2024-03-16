import discord
from discord.ext import commands

import config


class MessageListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        if message.author != self.bot.user:
            await message.author.guild.get_channel(config.LOG_CHANNEL).send(f"User: {message.author.mention} > "
                                                                             f"Message: `{message.content}` > "
                                                                             f"Channel: `{message.channel}`")

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        await before.author.guild.get_channel(config.LOG_CHANNEL).send(embed=message_edit_embed(before, after))


def message_edit_embed(before: discord.Message, after: discord.Message):
    embed = discord.Embed(
        title="Message Edited",
        timestamp=after.created_at
    )

    embed.add_field(name='Author', value=before.author.mention, inline=True)
    embed.add_field(name='Channel', value=before.channel.mention, inline=True)
    msg_link = f"https://discord.com/channels/{before.guild.id}/{before.channel.id}/{before.id}"
    embed.add_field(name='Message Reference', value=msg_link, inline=True)
    embed.add_field(name='Original Message', value=f"```{before.content}```", inline=False)
    embed.add_field(name='Edited Message', value=f"```{after.content}```", inline=False)

    embed.set_thumbnail(url='https://cdn-icons-png.freepik.com/512/1973/1973807.png ')

    return embed


def setup(bot): bot.add_cog(MessageListener(bot))
