import discord 
from discord.ext import commands
import asyncio
import sys
import os
import random
import helpembed

bot = commands.Bot(command_prefix = '$', case_insensitive=True)  #bot command prefix
bot.remove_command('help')

###Loading Cogs##########################################################################################

extensions=['moderation', 'veteran', 'general', 'verification']

if __name__ == '__main__':
    sys.path.insert(1, os.getcwd() + '/cogs/')
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Failed to load cogs : "+ e)



#EVENTS####################################################################################################

#Event: when bot becomes ready.
@bot.event  #event/function decorators
async def on_ready():
    print("Bot is ready")   #message which bot sends when it is ready


#Event: when any member joins the server 
@bot.event
async def on_member_join(member):   #a function which works when any member joins,need param `member`
    print(f'{member} has joined the server :)')
    channel = discord.utils.get(member.guild.channels, name="welcome")
    rchannel = discord.utils.get(member.guild.channels, name="obligatory-rules")
    await channel.send(f'***Hi there, {member.mention} Welcome to JHDiscord!***\n\nTo gain access to the rest of the server. please read the {rchannel.mention} and then verify yourself.\nTo Verify yourself, Please use command `$verify` and complete the **true or false quiz** that follows based off the obligatory rules.\n**Don\'t worry, If in case verification fails, our moderation team will be notified and will assist you.**\nThere is no need to ping us but you can still tell us if you face a problem in this channel\n\nAlso the JHD_Bot will send you a DM, so please make sure you have DM\'s from server members `on` in `privacy settings` before you use `$verify` command, thanks')

#On error Event
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command passed. Please Use `$help` to know valid commands")
    else:
        await ctx.send("There was an error, sorry! If you belive it's a mistake by bot, let our moderators/admins know about it")

@bot.event
async def on_message(message):
    if 'https://' in message.content.lower() or 'http://' in message.content.lower() or 'ftp://' in message.content.lower():
        if str(message.channel)=="resources":
            with open('/home/ubuntu/JHD_Resources/botfile.md','a+') as fa:
                fa.write("## "+str(message.author.name)+"\n")
                fa.write("Message : "+str(message.content)+"\n\n")
                fa.write("-----\n")
    else:
        await bot.process_commands(message)
        return
    await bot.process_commands(message)

################################################################################################################################################  
#JHDbot help message
@bot.command(name="help")       #alias of command name
async def _help(ctx, helprole=None):                              #role-vise help section
    role = discord.utils.get(ctx.author.roles, name="Veteran")
    coolpeople = discord.utils.get(ctx.author.roles, name="Cool People")
    if(str(ctx.message.channel)=="bot-commands" or role!=None or coolpeople!=None or ctx.message.author.guild_permissions.manage_messages):
        if helprole=="Veteran" or helprole=="veteran":                                   
            emb = discord.Embed(description=helpembed.veteranhelplist, colour=0xff002a)
            emb.set_author(name="JHDiscord Bot", icon_url=f"{ctx.guild.icon_url}")
            emb.set_thumbnail(url=f"{ctx.guild.icon_url}")
            emb.set_footer(text="Created by: JHD Moderation team ")
            await ctx.send(embed=emb)
        elif helprole=="Moderator" or helprole=="moderator":
            emb = discord.Embed(description=helpembed.moderatorhelplist, colour=0xff002a)
            emb.set_author(name="JHDiscord Bot", icon_url=f"{ctx.guild.icon_url}")
            emb.set_thumbnail(url=f"{ctx.guild.icon_url}")
            emb.set_footer(text="Created by: JHD Moderation team ")
            await ctx.send(embed=emb)
        else:
            emb=discord.Embed(title="John Hammond Discord", url="https://www.youtube.com/user/RootOfTheNull", description=helpembed.memberhelplist, color=0xff002a)
            emb.set_author(name="JHDiscord Bot", icon_url=f"{ctx.guild.icon_url}")
            emb.set_thumbnail(url=f"{ctx.guild.icon_url}")
            emb.set_footer(text="Created by: JHD Moderation team ")
            await ctx.send(embed=emb)
    else:
        await ctx.send("Please use this command in `#bot-commands`")

################################################################################################################################################  
#FAQ message
@bot.command(aliases=['qna'])
async def FAQ(ctx):
    role = discord.utils.get(ctx.author.roles, name="Veteran")
    coolpeople = discord.utils.get(ctx.author.roles, name="Cool People")
    if(str(ctx.message.channel)=="bot-commands" or role!=None or coolpeople!=None or ctx.message.author.guild_permissions.manage_messages):
        emb = discord.Embed(description=helpembed.faq, colour=0xff002a)
        emb.set_author(name="JHDiscord Bot", icon_url=f"{ctx.guild.icon_url}")
        emb.set_thumbnail(url=f"{ctx.guild.icon_url}")
        emb.set_footer(text="by: JHD Moderation team ")
        await ctx.send(embed=emb)
    else:
        await ctx.send("Please use this command in `#bot-commands`")

################################################################################################################################################  
#Channel desc message
@bot.command(aliases=['chdesc'])
async def Channeldesc(ctx):
    role = discord.utils.get(ctx.author.roles, name="Veteran")
    coolpeople = discord.utils.get(ctx.author.roles, name="Cool People")
    if(str(ctx.message.channel)=="bot-commands" or role!=None or coolpeople!=None or ctx.message.author.guild_permissions.manage_messages):
        emb = discord.Embed(description=helpembed.channels, colour=0xff002a)
        emb.set_author(name="JHDiscord Bot", icon_url=f"{ctx.guild.icon_url}")
        emb.set_thumbnail(url=f"{ctx.guild.icon_url}")
        emb.set_footer(text="by: JHD Moderation team ")
        await ctx.message.author.send(embed=emb)
        emb = discord.Embed(description=helpembed.channels2, colour=0xff002a)
        emb.set_author(name="JHDiscord Bot", icon_url=f"{ctx.guild.icon_url}")
        emb.set_thumbnail(url=f"{ctx.guild.icon_url}")
        emb.set_footer(text="by: JHD Moderation team ")
        await ctx.message.author.send(embed=emb)
    else:
        await ctx.send("Please use this command in `#bot-commands`")



### Token ###
bot.run("Njk4MjIxNTk2MTg3NTU3OTQw.XpCrmQ.DWu6ars9vZT5pLqW_Sva8I2FDCQ") #token
