import discord
from discord.ext import commands

import views.applyView


class ApplySetup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def apply_setup_cmd(self, ctx: discord.ApplicationContext):
        embed = discord.Embed(
            title="Apply Setup",
            description='Hello world'
        )
        await ctx.respond('Sending Application Setup Embed..', ephemeral=True)
        await ctx.delete(delay=3)
        await ctx.send(embed=embed, view=views.applyView.ApplySelector())


def setup(bot):
    bot.add_cog(ApplySetup(bot))
