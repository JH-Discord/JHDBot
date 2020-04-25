import discord 
from discord.ext import commands
import asyncio
from requests_html import HTML, HTMLSession
import requests
import re

class GeneralCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #GoogleSearchcommand ... IT works but we removed it because someone can search for explicit content too..
""" @commands.command(aliases=['google', 'g'])  
    async def letmegoogleitforya(self, ctx, *, input):
        flag=0
        linput=input.split(' ')
        swearwords = ['anus', 'arse', 'ballsack', 'bastard', 'biatch', 'blowjob', 'bollock', 'bollok', 'boner', 'buttplug', 'clitoris', 'cock', 'cunt', 'dick', 'dildo', 'dyke', 'fag', 'faggot', 'feck', 'fellate', 'fellatio', 'felching', 'fudgepacker', 'jizz', 'knobend', 'labia', 'muff', 'nigger', 'nigga', 'penis', 'pube', 'pussy', 'queer', 'scrotum','sh1t', 'slut', 'smegma', 'spunk', 'tit', 'tosser', 'turd', 'twat', 'vagina', 'wank', 'whore', 'tits', 'titty', 'fvck', 'asshat', 'pu55y', 'pen1s', 'bitch', 'fuck', 'sex', 'dickhead', 'pornhub.com', 'porn.com', 'xxxvideos.com', 'xvideos.com', 'porn', 'pornhub', 'xxxvideos', 'xvideos']
        for i in range(len(linput)):
            if(linput[i] in swearwords):
                flag+=1
            else:
                continue
        if(flag>=1):
            await ctx.message.author.send("You were warned in JHDiscord: Explicit search content found, if repeated, it will result in a bad")
            await ctx.channel.send("Explicit content found in search, further aado may result in a kick/ban !")
        else:
            coolpeople = discord.utils.get(ctx.author.roles, name="Cool People")
            role = discord.utils.get(ctx.author.roles, name="Veteran")
            if(ctx.channel=="bot-commands" or role!=None or coolpeople!=None or ctx.message.author.guild_permissions.manage_messages):
                session=HTMLSession()
                url="https://www.google.com/search?q="+input+"&safe=active"
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
            else:
                channel = discord.utils.get(ctx.author.guild.channels, name="bot-commands")
                await ctx.send(f"This command is only accessable in {channel.mention}")
"""

def setup(bot):
    bot.add_cog(GeneralCog(bot))
    print('General cog loaded')