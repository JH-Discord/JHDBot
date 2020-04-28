import discord 
from discord.ext import commands
import asyncio


class GeneralCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Ping Command to check if server is up or not
    @commands.command()       #creating Commands ctx is something like context, send automatically 
    async def ping(self, ctx):
        role = discord.utils.get(ctx.author.roles, name="Veteran")
        coolpeople = discord.utils.get(ctx.author.roles, name="Cool People")
        if(str(ctx.message.channel)=="bot-commands" or role!=None or coolpeople!=None or ctx.message.author.guild_permissions.manage_messages):
            await ctx.send(f"Ping - {round(bot.latency * 1000)}ms")
        else:
            await ctx.send("Please use this command in `#bot-commands`")

    #For Likt
    @commands.command()
    async def solve(self, ctx, *, input=None):
        role = discord.utils.get(ctx.author.roles, name="Veteran")
        coolpeople = discord.utils.get(ctx.author.roles, name="Cool People")
        if(str(ctx.message.channel)=="bot-commands" or role!=None or coolpeople!=None or ctx.message.author.guild_permissions.manage_messages):
            await ctx.send("That is a definite maybe")
        else:
            await ctx.send("Please use this command in `#bot-commands`")

    # Reportbot command
    @commands.command()
    async def reportbot(self, ctx, *,reason=None):
        coolpeople = discord.utils.get(ctx.author.roles, name="Cool People")
        if(str(ctx.message.channel)=="bot-commands" or coolpeople!=None or ctx.message.author.guild_permissions.manage_messages):
            if reason==None:
                await ctx.send("Invalid syntax, please add the issue you are facing.")
            else:
                creator = await bot.fetch_user(554907015785218050)
                await creator.send(f"Reported by user {ctx.message.author} : "+reason)
                await ctx.send("Your report has been successfully forwarded to moderators")
        else:
            await ctx.send("Please use this command in `#bot-commands`")

    #reporting users
    @commands.command()
    async def report(self, ctx, user=None, *,reason=None):
        coolpeople = discord.utils.get(ctx.author.roles, name="Cool People")
        if(str(ctx.message.channel)=="bot-commands" or coolpeople!=None or ctx.message.author.guild_permissions.manage_messages):
            if reason==None or user==None:
                await ctx.send("Invalid syntax, please check `$help` to check the syntax and pass proper arguments.")
            else:
                channel = discord.utils.get(ctx.message.author.guild.channels, name="moderators")
                await channel.send(f"Reported by user {ctx.message.author} : Complain against user {user} - "+reason)
                await ctx.send("Your report has been successfully forwarded to moderators")
        else:
            await ctx.send("Please use this command in `#bot-commands`")

def setup(bot):
    bot.add_cog(GeneralCog(bot))
    print('General cog loaded')