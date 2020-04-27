#!/usr/bin/python3
import discord 
from discord.ext import commands
import asyncio
import json
import sys
import time
import os
import random
import helpembed

bot = commands.Bot(command_prefix = '!', case_insensitive=True)  #bot command prefix
bot.remove_command('help')

###Loading Cogs##########################################################################################

extensions=['moderation', 'veteran',]

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
    rchannel = discord.utils.get(member.guild.channels, name="obligatory-rules")
    await channel.send(f'***Hi there, {member.mention} Welcome to JHDiscord!***\n\nTo gain access to the rest of the server. please read the {rchannel.mention} and then verify yourself.\nTo Verify yourself, Please use command `!verify` and complete the **true or false quiz** that follows based off the obligatory rules.\n**Don\'t worry, If in case verification fails, our moderation team will be notified and will assist you.\nThere is no need to ping us.**')

#On error Event
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command passed. Please Use `!help` to know valid commands")
    else:
        await ctx.send(f"There was an error, sorry! If you belive it's a mistake by bot, let our moderators/admins know about it")

###############################################################################
#Ping Command to check if server is up or not
@bot.command()       #creating Commands ctx is something like context, send automatically 
async def ping(ctx):
    await ctx.send(f"Ping - {round(bot.latency * 1000)}ms")

#For Likt
@bot.command()
async def solve(ctx, *, input):
    await ctx.send("That is a definite maybe")


################################################################################################################################################

"""    @bot.command()								#role verifictaion
    async def verify(ctx, *, input):
        try:
            data = json.loads(input)																					#take input data and put it in json format
            if(len(data['name'])==0 or len(data['Announcement role'])==0 or len(data['What brought you here?'])==0):	#check length of input if any value == null
                await ctx.send("Incomplete arguments, please re-verify yourself with proper inputs")					#prints Incomplete arguments
            elif(len(data['name'])>0 and len(data['Announcement role'])>0 and len(data['What brought you here?'])>0):	#search for Member roles from all the roles in server, guild==server
                if(data['name']=="<yournickname>" and data['Announcement role']=="(Yes|no)" and data['What brought you here?']=="<reason to join server>"):
                    await ctx.send("Default arguments passed, please re-verify yourself with proper inputs")
                else:            
                    role = discord.utils.get(ctx.guild.roles, name="Member")												
                    await ctx.message.author.add_roles(role)
                    await ctx.send("You are successfully verified")
                    if(data['Announcement role']=="Yes" or data['Announcement role']=="YES" or data['Announcement role']=="yes"):	#search for Member roles from all the roles in server, guild==server
                        role = discord.utils.get(ctx.guild.roles, name="Announcements")												#give announcement role to author of message i.e person who sended verfication message
                        await ctx.message.author.add_roles(role)	
                        await ctx.send("Announcement role succesfully given : )")        
            else:
                await ctx.send("Sorry, failed to authorize you, relax a moderator/admin will help you soon : )")			#error message because I am paranoid
        except:
            await ctx.send("Sorry, failed to authorize you, relax a moderator/admin will help you soon.")"""					#As I said, I am paranoid

################################################################################################################################################  
#JHDbot help message
@bot.command(name="help")       #alias of command name
async def _help(ctx, helprole=None):                         #can't figure out why I can't name command help #role-vise help section
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



###################################################################################################################
#Current Verification method
@bot.command(aliases=['verification'])
async def verify(ctx):
    gotindex=[]
    i=0
    flag=0
    if(str(ctx.message.channel)=="welcome"):
        await ctx.message.author.send("**Hey Again, I hope you ready for verification quiz**\nVerification quiz will start in `30` secound hope you have read the rules properly, also you will have `60` seconds to answer each question so please read the question properly : )\n\nDon't worry, if verification fail please go back to welcome channel and again type `!verify` to re-verify yourself, or just ask moderators for help.")
        time.sleep(35)
        while True:
            index=random.randint(0,20)
            if index not in gotindex:
                i+=1
                gotindex.append(index)
                question=helpembed.listofquestions[index]
                answer=helpembed.answers[index]
                await ctx.message.author.send("**Question : "+question+"[Answer as either `True` or `False`.]**")

                def check(m):
                    return m.author == ctx.message.author 

                try:
                    msg = await bot.wait_for('message', check=check, timeout = 60)
                    if msg.content.lower() == answer:
                        await ctx.message.author.send('Correct Answer\n')
                        time.sleep(1)
                    else:
                        await ctx.message.author.send('Wrong Answer.')
                        flag+=1
                        break
                except asyncio.TimeoutError:
                    await ctx.message.author.send('Times out')
                if i>=4:
                    break
            else:
                continue
        if(flag>=1):
            await ctx.message.author.send(f"{ctx.message.author.mention} Verification failed, it seems you gave a wrong answer leading to this fail, please go through rules again and re-verify yourself(you can again use `!verify` command to verify yourself), if you have any other question or if you want to be manually verified, please wait for our veterans/moderators/admins, they will help you as soon as they see your texts in this channel. Note: Please don't ping a role, our team is already notified. :)")
            channel = discord.utils.get(ctx.message.author.guild.channels, name="verifications-help")
            await channel.send(f"Seems like {ctx.message.author}, failed his verification.. If anyone is online and free atm, please help that member, thank ya.. I will owe you one :P")
            await channel.send(f"log: {ctx.message.author} failed on this question: {question}")
            await channel.send("...")
        else:
            announ=0
            await ctx.message.author.send("**Question: Do you also want announcement role ? [Answer as either `Yes` or `No`.]**")
            def check(m):
                return m.author == ctx.message.author 
            try:
                msg = await bot.wait_for('message', check=check, timeout = 60)
                if msg.content.lower() == "yes":
                    announ+=1
            except asyncio.TimeoutError:
                await ctx.message.author.send('Times out')
            role = discord.utils.get(ctx.guild.roles, name="Member")
            await ctx.message.author.add_roles(role)
            if(announ==1):
                role = discord.utils.get(ctx.guild.roles, name="Announcements")
                await ctx.message.author.add_roles(role)
            channel = discord.utils.get(ctx.message.author.guild.channels, name="bot-commands")
            await ctx.message.author.send(f'**Welcome to the Server, **{ctx.message.author.mention} **!** \nWe are glad to have you here. if you wanna go through quick server description please go to {channel.mention} and enter command `!chdesc` to get a description of almost every channel and `!faq` to get frequently asked questions.\nWe hope you enjoy your stay and contribute in our community : )')
    else:
        await ctx.send("Mate..You are already verified : )")

### Token ###
bot.run("Njk4MjIxNTk2MTg3NTU3OTQw.XpCrmQ.DWu6ars9vZT5pLqW_Sva8I2FDCQ") #token
