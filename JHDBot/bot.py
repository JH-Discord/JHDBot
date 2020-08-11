import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import sys
import os
import random
import helpembed
import logging
from webhook_loghandlers.handlers import DiscordHandler
#import configfile

load_dotenv()

bot = commands.Bot(command_prefix=str(os.environ.get('BOT_PREFIX_CHARACTER')), case_insensitive=True)  # bot command prefix
bot.remove_command('help')
# Loading Cogs

extensions = ['moderation', 'veteran', 'general', 'verification']

logger = logging.getLogger('Bot')
logger.setLevel(logging.INFO)
hookToken = os.getenv("LOGGING_WEBHOOK_TOKEN")
hookChannel = os.getenv("LOGGING_WEBHOOK_CHANNEL")
discordHandler = DiscordHandler(f'https://discordapp.com/api/webhooks/{hookChannel}/{hookToken}')
discordHandler.setLevel(logging.INFO)
formatter = logging.Formatter('[%(name)s] (%(levelname)s): %(message)s')
discordHandler.setFormatter(formatter)
logger.addHandler(discordHandler)

if __name__ == '__main__':
    sys.path.insert(1, os.getcwd() + '/cogs/')
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            logger.critical(f'Failed to load cogs: {e}')
            print(f'Failed to load cogs : {e}')


# EVENTS

# Event: when bot becomes ready.
@bot.event  # event/function decorators
async def on_ready():
    logger.info("Bot Ready")
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
    logchannel = discord.utils.get(member.guild.channels, name='join-leave')
    emb = discord.Embed(description=f'User - {member.mention}\nId - {member.id}', colour=0x3CFF4C)
    emb.set_author(name='Member Joined', icon_url=f"{member.avatar_url}")
    emb.set_footer(text=f'Join Log')
    await logchannel.send(embed=emb)

#on member leave logs
@bot.event
async def on_member_remove(member):  #a function which works when any member lefts,need param `member`
    logchannel = discord.utils.get(member.guild.channels, name='join-leave')
    emb = discord.Embed(description=f'User - {member.mention}\nId - {member.id}\n', colour=0xFF693C)
    emb.set_author(name='Member Left', icon_url=f"{member.avatar_url}")
    emb.set_footer(text=f'Leave Log')
    await logchannel.send(embed=emb)

#Voice channel logs
@bot.event
async def on_voice_state_update(member, before, after):
    logchannel = discord.utils.get(member.guild.channels, name='voice-channel')
    try:
        if(before.channel==None):
            emb = discord.Embed(description=f'{member.mention}** joined voice channel **{after.channel.mention}', colour=0x00DAB4)
            emb.set_author(name=f'{member}', icon_url=f"{member.avatar_url}")
            emb.set_footer(text=f'Voice Channel Log')
            await logchannel.send(embed=emb)
        elif(after.channel==None):
            emb = discord.Embed(description=f'{member.mention}** left voice channel **{before.channel.mention}', colour=0x00DAB4)
            emb.set_author(name=f'{member}', icon_url=f"{member.avatar_url}")
            emb.set_footer(text=f'Voice Channel Log')
            await logchannel.send(embed=emb)
        else:
            emb = discord.Embed(description=f'{member.mention}** changed voice from **{before.channel.mention}** to** {after.channel.mention}', colour=0x00DAB4)
            emb.set_author(name=f'{member}', icon_url=f"{member.avatar_url}")
            emb.set_footer(text=f'Voice Channel Log')
            await logchannel.send(embed=emb)
    except Exception as e:
        print(f'some weird exception bot gets mad about {e}')

#maintenance logs
@bot.event
async def on_guild_channel_delete(channel):  # channel delete logs
    logchannel = discord.utils.get(channel.guild.channels, name='maintenance')
    emb = discord.Embed(description=f'**#{channel.name} deleted in `{channel.category}`**', colour=0xC70600)
    emb.set_author(name=f'{channel.guild}', icon_url=f"{channel.guild.icon_url}")
    emb.set_footer(text=f'Maintenance Log')
    await logchannel.send(embed=emb)

@bot.event
async def on_guild_channel_create(channel):  # channel create logs
    logchannel = discord.utils.get(channel.guild.channels, name='maintenance')
    emb = discord.Embed(description=f'**#{channel.name} created in `{channel.category}`**', colour=0xC70600)
    emb.set_author(name=f'{channel.guild}', icon_url=f"{channel.guild.icon_url}")
    emb.set_footer(text=f'Maintenance Log')
    await logchannel.send(embed=emb)

#on message edit
@bot.event #Working
async def on_message_edit(before, after):
    logchannel = discord.utils.get(before.guild.channels, name='message-logs')
    if(before.content!=after.content):
        emb = discord.Embed(description=f'**Message edited in {before.channel.mention} at {after.edited_at}\n**\nMessage content Before\n```{before.content}```Message content After\n```{after.content}```[Jump to message]({after.jump_url})', colour=0xFF9C2E)
        emb.set_author(name=f'{before.author}', icon_url=f"{before.author.avatar_url}")
        emb.set_footer(text=f'Message Edit Log')
        await logchannel.send(embed=emb)

#on message delete
@bot.event  #Working
async def on_message_delete(message):
    logchannel = discord.utils.get(message.guild.channels, name='message-logs')
    emb = discord.Embed(description=f'**Message deleted in {message.channel.mention}**\nMessage Content\n```{message.content}```\n', colour=0xFF2E4A)
    emb.set_author(name=f'{message.author}', icon_url=f"{message.author.avatar_url}")
    emb.set_footer(text=f'Message Delete Log')
    await logchannel.send(embed=emb)

# On error Event
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command. Please use `$help` to know list current valid commands.')
    else:
        logger.info(f"Error parsing bot command in channel: <#{ctx.message.channel.id}>\n```\nAuthor: {ctx.message.author}\nMessage: {ctx.message.content}\n```")
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
    cool_people = discord.utils.get(ctx.author.roles, name='Moderator Emeritus')
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
    coolpeople = discord.utils.get(ctx.author.roles, name='Moderator Emeritus')
    if (str(
            ctx.message.channel) == 'bot-commands' or role is not None or coolpeople is not None
            or ctx.message.author.guild_permissions.manage_messages):
        emb = discord.Embed(description=helpembed.faq, colour=0xff002a)
        await attach_embed_info(ctx, emb)
        await ctx.send(embed=emb)
    else:
        await ctx.send('Please use this command in `#bot-commands`')


# Channel desc message
@bot.command(aliases=['chdesc', 'channeldesc'])
async def channel_desc(ctx):
    role = discord.utils.get(ctx.author.roles, name='Veteran')
    coolpeople = discord.utils.get(ctx.author.roles, name='Moderator Emeritus')
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

if __name__ == '__main__':


    TOKEN = os.getenv("DISCORD_API_TOKEN")

    bot.run(TOKEN)  # token
