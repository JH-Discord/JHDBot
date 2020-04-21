#!/usr/bin/python3
import discord 
from discord.ext import commands
import json

client = commands.Bot(command_prefix = '!')  #bot command prefix

#EVENTS####################################################################################################
#Event: when bot becomes ready.
@client.event  #event/function decorators
async def on_ready():
    print("Bot is ready")   #message which bot sends when it is ready


#Event: when any member joins the server 
@client.event
async def on_member_join(member):   #a function which works when any member joins,need param `member`
    print(f'{member} has joined the server :)')
    channel = client.get_channel(id=698224498796920885)
    await channel.send(f'***Hi there, {member.mention} Welcome to JHDiscord!***\n\nTo gain access to the rest of the server. please read the \#obligatory-rules and then verify yourself.\nTo Verify yourself, Please fill the info in this JSON formated string and use command\n`!verify <JSON string>` to verify yourself\n\nJSON formatted string```{{"name":"<yournickname>", "Announcement role":"(Yes|no)", "What brought you here?":"<reason to join server>"}}```\n***Don\'t worry, If in case verification fails, a moderator/admin will help you with it.***') #member.mention pings a user !

@client.event
async def on_member_leave(member):  #a function which works when any member lefts,need param `member`
    print(f'{member} has left the server :(')
    channel = client.get_channel(id=698224498796920885)
    await channel.send(f'Ah Goodbye {member}, you won\'t be missed') #doesn't print it, idk why

###############################################################################
#Ping Command to check if server is up or not
@client.command()       #creating Commands ctx is something like context, send automatically 
async def ping(ctx):
    await ctx.send(f"Ping - {round(client.latency * 1000)}ms")

#########################################TEMPSTUFFNEEDTOBEREMOVEDLATER##########
@client.command(aliases=['tm']) #aliases - other name for function/command
async def tellme(ctx, *, input):    # `*, input` takes all the input till the end of the line
    if(input=="Is Fume Awesome" or input=="is fume awesome"):
        await ctx.send(f"your input:{input} \nAnswer: Yes! He is heck awesome !") #says yes, because fume is awesome !
    else:
        await ctx.send(f"your input:{input} \nAnswer: NO") #replies No to everything user says ! 

    
##################################################################################
#beginner command
@client.command(aliases=['bgn'])       #creating Commands ctx is something like context, send automatically 
async def beginner(ctx):
    await ctx.send('I. Bandit OverTheWire: (https://overthewire.org/wargames/bandit/) A wargame focusing on basic Linux commands and privilege escalation. Questions can be asked in {#over-the-wire}\n\nII. PicoCTF: (https://picoctf.com/) A very beginner CTF that is up year round for practice. Questions can be asked in {#capture-the-flag} \n\nIII. Try Hack Me: (https://tryhackme.com/) A beginner friendly platform focusing on learning how to hack in more real world situations than CTFs. There are "rooms" for all levels and walkthroughs are available if necessary. Questions can be asked in {#tryhackme}\n\nIV. Natas OverTheWire: (https://overthewire.org/wargames/natas/) A wargame focusing on teaching the basics of server side web-security. Questions can also be asked in the {#over-the-wire} channel.\n\nFor any additional questions or concerns, please consult the {#beginners} channel')

############################################################################
#nypa command
@client.command(aliases=['nypa'])       #creating Commands ctx is something like context, send automatically 
async def notyourpersonalavengers(ctx):
    await ctx.send(f"We aren't your personal Avengers. You are going to need to use other methods for that. Customer support and local law enforcement are probably best depending on the circumstance.")

##################################################################################
#blackhat command
@client.command(aliases=['bt'])       #creating Commands ctx is something like context, send automatically 
async def blackhat(ctx):
    await ctx.send("Unfortunately it seems as though you are discussing blackhat activities. The term Blackhat refers to hacking for personal gain or to be generally malicious. Please refer to {#obligatory-rules} . We do not and cannot support illegal or immoral activities as mentioned above.")


##################################################################################
#account command
@client.command()       #creating Commands ctx is something like context, send automatically 
async def account(ctx):
    await ctx.send('Sorry. We can\'t help with account recovery. Your only path for that is to contact support for the respective service. "I forgot my password" is often a good place to start.')

##################################################################################
#ctfwhat command
@client.command()       #creating Commands ctx is something like context, send automatically 
async def ctfwhat(ctx):
    await ctx.send('CTF\'s are competitions you can participate into to practice and learn cybersecurity skills in a legal way. Here is a pretty cool video that explains them. https://www.youtube.com/watch?v=8ev9ZX9J45A&t=2s \n\nWargames are similar but run all the time where as CTFs tend to just run for a few days.')


################################################################################################################################################

@client.command()								#role verifictaion
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





@client.command() #a function to clear messages, if bot has perms to do that...
async def clear(cxt, amount=2):     #amount=2 sets the default value to 2 basically command + the text above that
    if (cxt.message.author.guild_permissions.manage_messages):
        await cxt.channel.purge(limit=amount+1) #limit= number of messages going to be deleted !
    else:
        await cxt.send("Sorry, it seems like you are not authorized to do it")

@client.command() #a functipn to kick members
async def kick(cxt, user: discord.Member, *, reason=None): #gets context user and reason, default being None
    if user.guild_permissions.manage_messages:  #check perms. if user has perms to manage message like if he mod he can't be kicked by the bot.
        await cxt.send(f"Sorry, can't kick {user} because of perms : (") 
    elif cxt.message.author.guild_permissions.kick_members: #checks if user who send the kick command is authorized to do it.
        await cxt.guild.kick(user=user, reason=reason)  #kicks that user
        await cxt.send(f'{user} has been kicked out from the server')
    else:
        await cxt.send("Sorry, it seems like you are not authorized to do it")

@client.command() #a functipn to ban members
async def ban(cxt, user: discord.Member, *, reason=None): #gets context user and reason, default being None
    if user.guild_permissions.manage_messages:  #check perms. if user has perms to manage message like if he mod he can't be banned by the bot.
        await cxt.send(f"Sorry, can't ban {user} because of perms : (") 
    elif cxt.message.author.guild_permissions.ban_members: #checks if user who send the ban command is authorized to do it.
        await cxt.guild.ban(user=user, reason=reason)  #bans that user
        await cxt.send(f'{user} has been banned from the server')
    else:
        await cxt.send("Sorry, it seems like you are not authorized to do it")


client.run("Njk4MjIxNTk2MTg3NTU3OTQw.XpCrmQ.DWu6ars9vZT5pLqW_Sva8I2FDCQ") #token
