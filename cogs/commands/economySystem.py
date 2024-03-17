import discord
from discord.ext import commands

import database


class EconomySystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    economy = discord.SlashCommandGroup('economy', 'Manage a users economy')

    @economy.command(name='add', description='Add balance to a user')
    async def add(self, ctx, target: discord.Member, value: int):

        coins = database.get_coins(target.id)
        if coins is None:
            database.add_user(target.id, value)
        else:
            database.set_coins(target.id, coins+value)

        await ctx.respond(f'Successfully added `{value}` coins to `{target.name}`')

    @economy.command(name='remove', description='Remove balance from a user')
    async def remove(self, ctx, target: discord.Member, value: int):

        coins = database.get_coins(target.id)
        if coins-value >= coins:
            database.delete_user(target.id)
        else:
            database.set_coins(target.id, coins-value)

        await ctx.respond(f'Successfully removed `{value}` coins from `{target.name}`')

    @economy.command(name='set', description='Set the balance of a user')
    async def set(self, ctx, target: discord.Member, value: int):
        print('set' + target.name + str(value))


def setup(bot): bot.add_cog(EconomySystem(bot))
