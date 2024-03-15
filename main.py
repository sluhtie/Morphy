import discord
import os
from dotenv import load_dotenv

from cogs.events.joinEvent import join_log_embed, leave_log_embed
from logger import logger

load_dotenv()  # load all the variables from the env file
bot = discord.Bot(intents=discord.Intents.all())

# Load all cogs
cogs = [
    "cogs.commands.userInfo",
    "cogs.commands.purgeMessages",
    "cogs.events.joinEvent"
]
for cog in cogs: bot.load_extension(cog) and logger.info(f'Loaded cog: {cog}')


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

    # await bot.get_channel(1109924971951685682).send(embed=join_log_embed(bot.get_guild(1000913517660098692).get_member(830057380359438396)))
    # await bot.get_channel(1109924971951685682).send(embed=leave_log_embed(bot.get_guild(1000913517660098692).get_member(830057380359438396)))

    # Change presence for each guild to member count
    for guildinstance in bot.guilds:
        await bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.playing,
            name=f"{guildinstance.member_count} members")
        )


bot.run(os.getenv('TOKEN'))  # run the bot with the token
