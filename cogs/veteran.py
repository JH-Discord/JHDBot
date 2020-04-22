import discord 
from discord.ext import commands
import asyncio

class VeteranCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #beginner command
    @commands.command(aliases=['bgn'])       #creating Commands ctx is something like context, send automatically 
    async def beginner(self, ctx):
        otw = discord.utils.get(ctx.guild.channels, name="over-the-wire")
        ctf = discord.utils.get(ctx.guild.channels, name="capture-the-flag")
        thm = discord.utils.get(ctx.guild.channels, name="tryhackme")
        big = discord.utils.get(ctx.guild.channels, name="beginners")
        role = discord.utils.get(ctx.author.roles, name="Veteran")
        if(role!=None):
            await ctx.send(f'I. Bandit OverTheWire: (https://overthewire.org/wargames/bandit/) A wargame focusing on basic Linux commands and privilege escalation. Questions can be asked in {otw.mention}\n\nII. Natas OverTheWire: (https://overthewire.org/wargames/natas/) A wargame focusing on teaching the basics of server side web-security. Questions can also be asked in the {otw.mention} channel.\n\nIII. PicoCTF: (https://picoctf.com/) A very beginner CTF that is up year round for practice. Questions can be asked in {ctf.mention} \n\nIV. Try Hack Me: (https://tryhackme.com/) A beginner friendly platform focusing on learning how to hack in more real world situations than CTFs. There are "rooms" for all levels and walkthroughs are available if necessary. Questions can be asked in {thm.mention}\n\n For any additional questions or concerns, please consult the {big.mention} channel')
        elif(ctx.message.author.guild_permissions.manage_messages):
            await ctx.send(f'I. Bandit OverTheWire: (https://overthewire.org/wargames/bandit/) A wargame focusing on basic Linux commands and privilege escalation. Questions can be asked in {otw.mention}\n\nII. Natas OverTheWire: (https://overthewire.org/wargames/natas/) A wargame focusing on teaching the basics of server side web-security. Questions can also be asked in the {otw.mention} channel.\n\nIII. PicoCTF: (https://picoctf.com/) A very beginner CTF that is up year round for practice. Questions can be asked in {ctf.mention} \n\nIV. Try Hack Me: (https://tryhackme.com/) A beginner friendly platform focusing on learning how to hack in more real world situations than CTFs. There are "rooms" for all levels and walkthroughs are available if necessary. Questions can be asked in {thm.mention}\n\n For any additional questions or concerns, please consult the {big.mention} channel')
        else:
            await ctx.send('Seems like you are not authorized to use this command D:')


    #nypa command
    @commands.command(aliases=['nypa'])       #creating Commands ctx is something like context, send automatically 
    async def notyourpersonalavengers(self, ctx):
        role = discord.utils.get(ctx.author.roles, name="Veteran")
        if(role!=None):
            await ctx.send("We aren't your personal Avengers. You are going to need to use other methods for that. Customer support and local law enforcement are probably best depending on the circumstance.")
        elif(ctx.message.author.guild_permissions.manage_messages):
            await ctx.send("We aren't your personal Avengers. You are going to need to use other methods for that. Customer support and local law enforcement are probably best depending on the circumstance.")
        else:
            await ctx.send('Seems like you are not authorized to use this command D:')


    #blackhat command
    @commands.command(aliases=['bt'])       #creating Commands ctx is something like context, send automatically 
    async def blackhat(self, ctx):
        role = discord.utils.get(ctx.author.roles, name="Veteran")
        channel = discord.utils.get(ctx.guild.channels, name="obligatory-rules")
        if(role!=None):
            await ctx.send(f'Unfortunately it seems as though you are discussing blackhat activities. The term Blackhat refers to hacking for personal gain or to be generally malicious. Please refer to {channel.mention} . We do not and cannot support illegal or immoral activities as mentioned above.')
        elif(ctx.message.author.guild_permissions.manage_messages):
            await ctx.send(f'Unfortunately it seems as though you are discussing blackhat activities. The term Blackhat refers to hacking for personal gain or to be generally malicious. Please refer to {channel.mention} . We do not and cannot support illegal or immoral activities as mentioned above.')
        else:
            await ctx.send('Seems like you are not authorized to use this command D:')


    #account command
    @commands.command()       #creating Commands ctx is something like context, send automatically 
    async def account(self, ctx):
        role = discord.utils.get(ctx.author.roles, name="Veteran")
        if(role!=None):
            await ctx.send('Sorry. We can\'t help with account recovery. Your only path for that is to contact support for the respective service. "I forgot my password" is often a good place to start.')
        elif(ctx.message.author.guild_permissions.manage_messages):
            await ctx.send('Sorry. We can\'t help with account recovery. Your only path for that is to contact support for the respective service. "I forgot my password" is often a good place to start.')
        else:
            await ctx.send('Seems like you are not authorized to use this command D:')


    #ctfwhat command
    @commands.command()       #creating Commands ctx is something like context, send automatically 
    async def ctfwhat(self, ctx):
        role = discord.utils.get(ctx.author.roles, name="Veteran")
        if(role!=None):
            await ctx.send('CTF\'s are competitions you can participate into to practice and learn cybersecurity skills in a legal way. Here is a pretty cool video that explains them. https://www.youtube.com/watch?v=8ev9ZX9J45A&t=2s \n\nWargames are similar but run all the time where as CTFs tend to just run for a few days.')
        elif(ctx.message.author.guild_permissions.manage_messages):
            await ctx.send('CTF\'s are competitions you can participate into to practice and learn cybersecurity skills in a legal way. Here is a pretty cool video that explains them. https://www.youtube.com/watch?v=8ev9ZX9J45A&t=2s \n\nWargames are similar but run all the time where as CTFs tend to just run for a few days.')
        else:
            await ctx.send('Seems like you are not authorized to use this command D:')


def setup(bot):
    bot.add_cog(VeteranCog(bot))
    print('Veteran cog loaded')