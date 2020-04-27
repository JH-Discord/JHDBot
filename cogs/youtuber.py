import discord 
from discord.ext import commands
import asyncio
from requests_html import HTML, HTMLSession
import requests
import re
import pytz
import datetime
import sqlite3
import cogs.streamlists

class YoutuberCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


"""    #Add stream feature
    @commands.command()
    async def addstream(self, ctx, name, link, year, month, date, hr, mins, sec):
        time = datetime.datetime(int(year), int(month), int(date), int(hr), int(mins), int(sec), tzinfo=pytz.UTC)
        timenow = datetime.datetime.now(tz=pytz.UTC)
        print(timenow-time)
        daysahead=re.compile(r'\d+\s').search(str(time-timenow)).group(0)
        if(int(daysahead)>=2):
            await ctx.send("Failed: Sorry a stream can only be added 2 days prior to the stream day, not before that")
            return
        youtubers = discord.utils.get(ctx.author.roles, name="Youtuber")
        if(youtubers!=None):
            db= sqlite3.connect("youtubers.sqlite")
            cursor = db.cursor()
            sql= ("Insert into youtubers(Name, link, time) values(?,?,?)")
            val= (name, link, time)
            cursor.execute(sql,val)
            db.commit()
            db.close
            await ctx.send("Stream Information succesfully added")
        else:
            await ctx.send("Sorry, it seems like you are not authorized to use this command :' (")

    #Show stream feature
    @commands.command()
    async def showstreams(self, ctx):
        db= sqlite3.connect("youtubers.sqlite")
        cursor = db.cursor()
        cursor.execute("select Name from youtubers")
        result=cursor.fetchone()
        if result==None:
            await ctx.send("Seems like the stream list is empty D:\n_Ask John to do more streams/premiures..lol_")
            return
        else:
            cursor.execute("select * from youtubers")
            result=cursor.fetchall()
            for x in range(len(result)):
                tup=result[x]
                emb = discord.Embed(description="**Youtuber : "+tup[0]+"\nLink : "+tup[1]+"\nTime : "+tup[2]+"**", colour=0xff002a)
                emb.set_thumbnail(url=f"{ctx.guild.icon_url}")
                await ctx.send(embed=emb)"""
        

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
    bot.add_cog(YoutuberCog(bot))
    print('Youtube useless cog loaded')