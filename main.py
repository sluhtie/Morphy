import pathlib

import discord
import os

from dotenv import load_dotenv
from logger import logger

load_dotenv()  # load all the variables from the env file
bot = discord.Bot(intents=discord.Intents.all())

# for cog in (cogs := [cog for cog in pathlib.Path('cogs').iterdir() if cog.name != '__pycache__']):
for cog in ["cogs.userInfo", "cogs.purgeMessages"]:
    try:
        bot.load_extension(cog)
        logger.info(f'Loaded cog: {cog}')
    except FileNotFoundError as ex:
        logger.error(f"Error. The file does not exist: {ex}")
    except PermissionError as ex:
        logger.error(f"Error: Permission denied: {ex}")
    except OSError as ex:
        logger.error(f"Error. OS Error: {ex}")
    except Exception as ex:
        logger.error(f"An unexpected Error occurred: {ex}")


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


bot.run(os.getenv('TOKEN'))  # run the bot with the token
