import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import sys
import os
import random
import helpembed

load_dotenv()

bot = commands.Bot(command_prefix=os.environ.get('command_prefix'), case_insensitive=True)  # bot command prefix
bot.remove_command('help')
# Loading Cogs

extensions = ['moderation', 'veteran', 'general', 'verification']

if __name__ == '__main__':
    sys.path.insert(1, os.getcwd() + '/cogs/')
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load cogs : {e}')


# EVENTS

# Event: when bot becomes ready.
@bot.event  # event/function decorators
async def on_ready():
    print('Bot is ready')  # message which bot sends when it is ready


# Event: when any member joins the server
@bot.event
async def on_member_join(member):  # a function which works when any member joins,need param `member`
    print(f'{member} has joined the server :)')
    if str(member.name) == 'username123':
        channel = discord.utils.get(member.guild.channels, name='moderators')
        await channel.send(f'Warning : {member.mention} arrived in the server!')
        channel2 = discord.utils.get(member.guild.channels, name="veteran-chat")
        await channel2.send(f'Warning : {member.mention} arrived in the server!')
    channel = discord.utils.get(member.guild.channels, name='welcome')
    rules_channel = discord.utils.get(member.guild.channels, name='obligatory-rules')
    await channel.send(
        f'***Hi there, {member.mention} Welcome to JHDiscord!***\n\nTo gain access to the rest of the server. please '
        f'read the {rules_channel.mention} and then verify yourself.\nTo Verify yourself, Please use command '
        f'`$verify` and '
        f'complete the **true or false quiz** that follows based off the obligatory rules.\n**Don\'t worry, '
        f'If in case verification fails, our moderation team will be notified and will assist you.**\nThere is no '
        f'need to ping us but you can still tell us if you face a problem in this channel\n\nAlso the JHD_Bot will '
        f'send you a DM, so please make sure you have DM\'s from server members `on` in `privacy settings` before you '
        f'use `$verify` command, thanks')


# On error Event
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command. Please use `$help` to know list current valid commands.')
    else:
        await ctx.send(
            f'An error occurred. Please use `{bot.command_prefix}reportbot <Error>`')


@bot.event
async def on_message(message):
    if 'https://' in message.content.lower() or 'http://' in message.content.lower() or 'ftp://' in message.content.lower():
        if str(message.channel) == "resources":
            with open('/home/ubuntu/JHD_Resources/botfile.md', 'a+') as fa:
                fa.write("## " + str(message.author.name) + "\n")
                fa.write("Message : " + str(message.content) + "\n\n")
                fa.write("-----\n")
    else:
        await bot.process_commands(message)
        return
    await bot.process_commands(message)


# JHDbot help message
@bot.command(name="help")  # alias of command name
async def _help(ctx, helprole=None):  # role-vise help section
    role = discord.utils.get(ctx.author.roles, name='Veteran')
    cool_people = discord.utils.get(ctx.author.roles, name='Cool People')
    if (str(
            ctx.message.channel) == 'bot-commands' or role is not None or cool_people is not None
            or ctx.message.author.guild_permissions.manage_messages):
        help_roles = ['Veteran', 'veteran', 'Moderator', 'moderator']
        if helprole in help_roles:
            if helprole == 'Veteran' or helprole == 'veteran':
                emb = discord.Embed(description=helpembed.veteranhelplist, colour=0xff002a)
            elif helprole == 'Moderator' or helprole == 'moderator':
                emb = discord.Embed(description=helpembed.moderator_help_list, colour=0xff002a)
            await attach_embed_info(ctx, emb)
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title='John Hammond Discord', url='https://www.youtube.com/user/RootOfTheNull',
                                description=helpembed.memberhelplist, color=0xff002a)
            await attach_embed_info(ctx, emb)
            await ctx.send(embed=emb)
    else:
        await ctx.send('Please use this command in `#bot-commands`')


# FAQ message
@bot.command(aliases=['qna'])
async def faq(ctx):
    role = discord.utils.get(ctx.author.roles, name='Veteran')
    coolpeople = discord.utils.get(ctx.author.roles, name='Cool People')
    if (str(
            ctx.message.channel) == 'bot-commands' or role is not None or coolpeople is not None
            or ctx.message.author.guild_permissions.manage_messages):
        emb = discord.Embed(description=helpembed.faq, colour=0xff002a)
        await attach_embed_info(ctx, emb)
        await ctx.send(embed=emb)
    else:
        await ctx.send('Please use this command in `#bot-commands`')


# Channel desc message
@bot.command(aliases=['chdesc'])
async def channel_desc(ctx):
    role = discord.utils.get(ctx.author.roles, name='Veteran')
    coolpeople = discord.utils.get(ctx.author.roles, name='Cool People')
    if (str(
            ctx.message.channel) == 'bot-commands' or role is not None or coolpeople is not None
            or ctx.message.author.guild_permissions.manage_messages):

        emb = discord.Embed(description=helpembed.channels, colour=0xff002a)
        await attach_embed_info(ctx, emb)
        await ctx.message.author.send(embed=emb)
        emb = discord.Embed(description=helpembed.channels2, colour=0xff002a)
        await attach_embed_info(ctx, emb)
        await ctx.message.author.send(embed=emb)
    else:
        await ctx.send('Please use this command in `#bot-commands`')


async def attach_embed_info(ctx=None, embed=None):
    embed.set_author(name='JHDiscord Bot', icon_url=f'{ctx.guild.icon_url}')
    embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
    embed.set_footer(text='by: JHD Moderation team ')
    return embed

# Token
bot.run(os.environ.get('bot_token'))  # token
