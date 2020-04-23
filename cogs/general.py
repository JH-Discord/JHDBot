import discord 
from discord.ext import commands
import asyncio
from requests_html import HTML, HTMLSession
import requests
import re

class GeneralCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #GoogleSearchcommand
    @commands.command(aliases=['google', 'g'])
    async def letmegoogleitforya(self, ctx, *, input):
        session=HTMLSession()
        url="https://www.google.com/search?q="+input
        r=session.get(url)
        try:
            if r.status_code==200:
                match = r.html.find('#result-stats', first=True)
                await ctx.send("**Fetched - "+ str((match.text)[:-14])+"**")
                await ctx.send("Here are the top 5 results for you..")
                results = r.html.find('div.g')
                for i in range(6):
                    if i==1:
                        continue
                    itter=i+1
                    if(i>=1):
                        itter=itter-1
                    link = results[i].find('a', first=True)
                    await ctx.send("**"+str(itter)+". link - **"+link.attrs['href'])        
            else:
                await ctx.send("Sorry, unable to fetch results")
        except:
            await ctx.send("Sorry, unable to fetch results")


def setup(bot):
    bot.add_cog(GeneralCog(bot))
    print('General cog loaded')