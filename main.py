import discord
import os  # default module
from dotenv import load_dotenv

import cogs.userInfo

load_dotenv()  # load all the variables from the env file
bot = discord.Bot(intents=discord.Intents.all())

for cog in ['cogs.userInfo']: bot.load_extension(cog)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
    module = cogs.userInfo
    await ctx.respond(embed=module.get_user_info(ctx.author))


bot.run(os.getenv('TOKEN'))  # run the bot with the token
