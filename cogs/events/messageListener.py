import discord
from discord.ext import commands


class MessageListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        if message.author != self.bot.user:
            await message.author.guild.get_channel(1109924971951685682).send(f"User: {message.author.mention} > "
                                                                             f"Message: `{message.content}` > "
                                                                             f"Channel: `{message.channel}`")

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        message_new = before.content
        message_old = after.content


def setup(bot): bot.add_cog(MessageListener(bot))
