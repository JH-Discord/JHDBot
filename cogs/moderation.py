import discord 
from discord.ext import commands
import asyncio

class ModeratorCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    #Clear Message Command..
    @commands.command() #a function to clear messages, if bot has perms to do that...
    async def clear(self, ctx, amount=2):     #amount=2 sets the default value to 2 basically command + the text above that
        try:
            if (ctx.message.author.guild_permissions.manage_messages):
                await ctx.channel.purge(limit=amount+1) #limit= number of messages going to be deleted !
                await ctx.channel.send(f"Deleted {amount} messages D:")
            else:
                await ctx.send("Sorry, it seems like you are not authorized to do it")
            await asyncio.sleep(5)
            await ctx.message.delete()
        except:
            await ctx.send("The bot is unauthorized to delete messages D:")


    #Mute Command..
    @commands.command() #a function to mute members
    async def mute(self, ctx, user: discord.Member, seconds=None):                      #gets context user and time(in seconds), default being None
        try:
            if ctx.message.author.guild_permissions.kick_members: 
                if seconds==None or int(seconds)<0:
                    await ctx.send("Please also supply time in seconds(proper +ve int format plz).")                        #if no time suplied, function exits
                    return
                else:
                    if user.guild_permissions.manage_messages:                                  #check perms. if user has perms to manage message like if he mod he can't be muted by the bot.
                        await ctx.send(f"Sorry, can't mute {user} because of perms : (") 
                        return
                    #add mute role
                    role = discord.utils.get(ctx.guild.roles, name="Muted")
                    mrole = discord.utils.get(ctx.guild.roles, name="Member")
                    await user.add_roles(role)
                    await user.remove_roles(mrole)
                    await user.send("You were muted in JHDiscord for `"+str(seconds)+"` seconds")
                    await ctx.send(f"{user} has been muted in JHD for `{seconds}` seconds")
                    muted = discord.utils.get(user.roles, name="Muted")
                    if(muted!=None):
                        await asyncio.sleep(int(seconds))
                        await user.remove_roles(role)
                        await user.add_roles(mrole)
                        await user.send("You were un-muted in JHDiscord, we hope you don't repeat the actions that lead the mods/admin to mute you.")
                        await ctx.send(f"{user} has been unmuted in JHD")
            else:
                await ctx.send("Sorry, it seems like you are not authorized to do it")
        except:
            await ctx.send("Seems like the Bot is not authorized to run this command")

    #unmute command..
    @commands.command()
    async def unmute(self, ctx, user: discord.Member):
        try:
            if ctx.message.author.guild_permissions.kick_members:
                muted = discord.utils.get(user.roles, name="Muted")
                if(muted!=None):
                    role = discord.utils.get(ctx.guild.roles, name="Muted")
                    mrole = discord.utils.get(ctx.guild.roles, name="Member")
                    await user.remove_roles(role)
                    await user.add_roles(mrole)
                    await user.send("You were un-muted in JHDiscord, we hope you don't repeat the actions that lead the mods/admin to mute you.")
                    await ctx.send(f"{user} has been unmuted in JHD")
                else:
                    await ctx.send(f"{user} is not muted ¯\_(ツ)_/¯ ")
            else:
                await ctx.send("Sorry, it seems like you are not authorized to do it")
            await asyncio.sleep(5)
            await ctx.message.delete()
        except:
            await ctx.send("Seems like the Bot is not authorized to run this command") 

    #Kick Member Command..
    @commands.command() #a function to kick members
    async def kick(self, ctx, user: discord.Member, *, reason=None):                      #gets context user and reason, default being None
        try:
            if user.guild_permissions.manage_messages:                                  #check perms. if user has perms to manage message like if he mod he can't be kicked by the bot.
                await ctx.send(f"Sorry, can't kick {user} because of perms : (") 
            elif ctx.message.author.guild_permissions.kick_members:                     #checks if user who send the kick command is authorized to do it.
                await user.send("You were kicked from JHDiscord :"+reason)
                await user.send("https://tenor.com/view/anime-kick-go-out-gif-14290462")
                await ctx.guild.kick(user=user, reason=reason)                          #kicks that user
                await ctx.send(f'{user} has been kicked out from the server')
                await ctx.send("https://tenor.com/view/anime-kick-go-out-gif-14290462")
            else:
                await ctx.send("Sorry, it seems like you are not authorized to do it")
            await asyncio.sleep(5)
            await ctx.message.delete()
        except:
            await ctx.send("The bot is unauthorized to kick members D:")


    #Ban Member Command..
    @commands.command() #a function to ban members
    async def ban(self, ctx, user: discord.Member, *, reason=None): #gets context user and reason, default being None
        try:
            if user.guild_permissions.manage_messages:  #check perms. if user has perms to manage message like if he mod he can't be banned by the bot.
                await ctx.send(f"Sorry, can't ban {user} because of perms : (") 
            elif ctx.message.author.guild_permissions.ban_members: #checks if user who send the ban command is authorized to do it.
                await user.send("You were banned from JHDiscord :"+reason)
                await user.send("https://tenor.com/view/blob-banned-ban-hammer-blob-ban-emoji-gif-16021044")
                await ctx.guild.ban(user=user, reason=reason)  #bans that user
                await ctx.send(f'{user} has been banned from the server')
                await ctx.send("https://tenor.com/view/blob-banned-ban-hammer-blob-ban-emoji-gif-16021044")
            else:
                await ctx.send("Sorry, it seems like you are not authorized to do it")
            await asyncio.sleep(5)
            await ctx.message.delete()
        except:
            await ctx.sent("The bot is unauthorized to ban members D:")

def setup(bot):
    bot.add_cog(ModeratorCog(bot))
    print('Moderation cog loaded')
