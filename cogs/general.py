import discord 
from discord.ext import commands
import asyncio

class GeneralCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(GeneralCog(bot))
    print('General cog loaded')