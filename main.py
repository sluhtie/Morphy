import discord
import os
from dotenv import load_dotenv
from logger import logger

load_dotenv()  # load all the variables from the env file
bot = discord.Bot(intents=discord.Intents.all())

# Load all cogs
cogs = [
    "cogs.commands.userInfo",
    "cogs.commands.purgeMessages",
    "cogs.events.joinLeaveListener",
    "cogs.events.messageListener",
    "cogs.events.channelListener"
]
for cog in cogs:
    bot.load_extension(cog)
    logger.info(f'Loaded cog: {cog}')


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

    # Change presence for each guild to member count
    for guildinstance in bot.guilds:
        await bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.playing,
            name=f"{guildinstance.member_count} members")
        )


bot.run(os.getenv('TOKEN'))  # run the bot with the token
