import discord
from discord.ext import commands


class PurgeMessages(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name='purge', description='Purges last x messages in chat')
    async def purge_messages_cmd(self, ctx, amount: discord.Option(int)):
        if ctx.author.guild_permissions.manage_messages:
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f'{amount} Nachricht(en) wurden gelöscht.', delete_after=5)
        else:
            await ctx.send("Du hast keine Berechtigung, Nachrichten zu löschen.")


def setup(bot):
    bot.add_cog(PurgeMessages(bot))
