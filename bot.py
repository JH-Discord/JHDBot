#!/usr/bin/python3
import discord 
from discord.ext import commands
import asyncio
import json
import sys
import os
import helpembed

bot = commands.Bot(command_prefix = '!', case_insensitive=True)  #bot command prefix
bot.remove_command('help')

###Loading Cogs##########################################################################################

extensions=['moderation', 'veteran','general']

if __name__ == '__main__':
    sys.path.insert(1, os.getcwd() + '/cogs/')
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Failed to load cogs : e")



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
    await channel.send(f'***Hi there, {member.mention} Welcome to JHDiscord!***\n\nTo gain access to the rest of the server. please read the \#obligatory-rules and then verify yourself.\nTo Verify yourself, Please fill the info in this JSON formated string and use command\n`!verify <JSON string>` to verify yourself\n\nJSON formatted string```{{"name":"<yournickname>", "Announcement role":"(Yes|no)", "What brought you here?":"<reason to join server>"}}```\n***Don\'t worry, If in case verification fails, a moderator/admin will help you with it.***') #member.mention pings a user !


###############################################################################
#Ping Command to check if server is up or not
@bot.command()       #creating Commands ctx is something like context, send automatically 
async def ping(ctx):
    await ctx.send(f"Ping - {round(bot.latency * 1000)}ms")


################################################################################################################################################

@bot.command()								#role verifictaion
async def verify(ctx, *, input):
    try:
        data = json.loads(input)																					#take input data and put it in json format
        if(len(data['name'])==0 or len(data['Announcement role'])==0 or len(data['What brought you here?'])==0):	#check length of input if any value == null
            await ctx.send("Incomplete arguments, please re-verify yourself with proper inputs")					#prints Incomplete arguments
        elif(len(data['name'])>0 and len(data['Announcement role'])>0 and len(data['What brought you here?'])>0):	#search for Member roles from all the roles in server, guild==server
            role = discord.utils.get(ctx.guild.roles, name="Member")												#give role to author of message i.e person who sended verfication message
            await ctx.message.author.add_roles(role)
            await ctx.send("You are successfully verified")
            if(data['Announcement role']=="Yes" or data['Announcement role']=="YES" or data['Announcement role']=="yes"):	#search for Member roles from all the roles in server, guild==server
                role = discord.utils.get(ctx.guild.roles, name="Announcements")												#give announcement role to author of message i.e person who sended verfication message
                await ctx.message.author.add_roles(role)	
                await ctx.send("Announcement role succesfully given : )")        
        else:
            await ctx.send("Sorry, failed to authorize you, relax a moderator/admin will help you soon : )")			#error message because I am paranoid
    except:
        await ctx.send("Sorry, failed to authorize you, relax a moderator/admin will help you soon.")					#As I said, I am paranoid

################################################################################################################################################  
#JHDbot help message
@bot.command(name="help")       #alias of command name
async def _help(ctx, role=None):                         #can't figure out why I can't name command help #role-vise help section
    if role=="Veteran" or role=="veteran":                                   
        emb = discord.Embed(description=helpembed.veteranhelplist, colour=0xff002a)
        emb.set_author(name="JHDiscord Bot", icon_url=f"{ctx.guild.icon_url}")
        emb.set_thumbnail(url=f"{ctx.guild.icon_url}")
        emb.set_footer(text="Created by: JHD Moderation team ")
        await ctx.send(embed=emb)
    elif role=="Moderator" or role=="moderator":
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



### Token ###
bot.run("Njk4MjIxNTk2MTg3NTU3OTQw.XpCrmQ.DWu6ars9vZT5pLqW_Sva8I2FDCQ") #token
