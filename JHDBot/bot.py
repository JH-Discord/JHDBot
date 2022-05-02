#!/usr/bin/env python3
import datetime
import sys
import os
import io
import re
import traceback
import discord
import aiohttp
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = Intents.default()
intents.members = True

bot = commands.Bot(
    command_prefix=str(os.environ.get("BOT_PREFIX_CHARACTER")), case_insensitive=True, intents=intents
)  # bot command prefix
bot.remove_command("help")
# Loading Cogs

extensions = ["moderation", "veteran", "general", "verification"]

hookToken = os.getenv("LOGGING_WEBHOOK_TOKEN")
hookChannel = os.getenv("LOGGING_WEBHOOK_CHANNEL")


if __name__ == "__main__":
    sys.path.insert(1, os.getcwd() + "/cogs/")
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            embed = discord.Embed(
                title="Failed To Load Cogs",
                color=0xFF0000,
                timestamp=datetime.datetime.now(datetime.timezone.utc),
            )

            exc_type, exc_value, exc_traceback = sys.exc_info()
            exception_text = "".join(
                traceback.format_exception(exc_type, exc_value, exc_traceback)
            )

            print(exception_text, file=sys.stderr)

            field_len = 1000
            fields = [
                exception_text[i : i + field_len]
                for i in range(0, len(exception_text), field_len)
            ]

            for i, field in enumerate(fields):
                f_name = "Traceback:" if i == 0 else "Continued:"
                embed.add_field(name=f_name, value=f"```{field}```", inline=False)

            webhook = discord.Webhook.from_url(
                f"https://discordapp.com/api/webhooks/{hookChannel}/{hookToken}",
                adapter=discord.RequestsWebhookAdapter(),
            )
            webhook.send(embed=embed)
            print(f"Failed to load cogs : {e}", file=sys.stderr)


# EVENTS

# Event: when bot becomes ready.
@bot.event  # event/function decorators
async def on_ready():
    embed = discord.Embed(
        title=f'Bot Started At:\n{datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M")} UTC',
        color=0x00FF00,
        timestamp=datetime.datetime.now(datetime.timezone.utc),
    )

    async with aiohttp.ClientSession() as s:
        webhook = discord.Webhook.from_url(
            f"https://discordapp.com/api/webhooks/{hookChannel}/{hookToken}",
            adapter=discord.AsyncWebhookAdapter(s),
        )
        await webhook.send(embed=embed)

    print("Bot is ready")  # message which bot sends when it is ready


# Event: when any member joins the server
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name=os.getenv("WELCOME_CHANNEL"))
    rules_channel = discord.utils.get(member.guild.channels, name=os.getenv("RULES_CHANNEL"))
    await channel.send(
        f'**Hi there, {member.mention} Welcome to JHDiscord!**\n\nTo gain access to the rest of the server. '
        f'Please read the {rules_channel.mention} and then verify yourself to join the conversation.\n')
    logchannel = discord.utils.get(member.guild.channels, name='join-leave')
    emb = discord.Embed(description=f'User - {member.mention}\nId - {member.id}', colour=0x3CFF4C)
    emb.set_author(name='Member Joined', icon_url=f"{member.avatar_url}")
    emb.set_footer(text=f'Join Log')
    await logchannel.send(embed=emb)


# on member leave logs
@bot.event
async def on_member_remove(member):
    logchannel = discord.utils.get(member.guild.channels, name="join-leave")
    emb = discord.Embed(
        description=f"User - {member.mention}\nId - {member.id}\n", colour=0xFF693C
    )
    emb.set_author(name="Member Left", icon_url=f"{member.avatar_url}")
    emb.set_footer(text="Leave Log")
    await logchannel.send(embed=emb)


# Voice channel logs
@bot.event
async def on_voice_state_update(member, before, after):
    logchannel = discord.utils.get(member.guild.channels, name="voice-channel")
    role = discord.utils.get(member.guild.roles, name="voice-text")
    if before.channel == None:
        emb = discord.Embed(
            description=f"{member.mention}** joined voice channel **{after.channel.mention}",
            colour=0x00DAB4,
        )
        emb.set_author(name=f"{member}", icon_url=f"{member.avatar_url}")
        emb.set_footer(text="Voice Channel Log")
        await logchannel.send(embed=emb)
        await member.add_roles(role)
    elif after.channel == None:
        emb = discord.Embed(
            description=f"{member.mention}** left voice channel **{before.channel.mention}",
            colour=0x00DAB4,
        )
        emb.set_author(name=f"{member}", icon_url=f"{member.avatar_url}")
        emb.set_footer(text="Voice Channel Log")
        await logchannel.send(embed=emb)
        await member.remove_roles(role)
    else:
        emb = discord.Embed(
            description=f"{member.mention}** changed voice from **{before.channel.mention}** to** {after.channel.mention}",
            colour=0x00DAB4,
        )
        emb.set_author(name=f"{member}", icon_url=f"{member.avatar_url}")
        emb.set_footer(text="Voice Channel Log")
        await logchannel.send(embed=emb)


# maintenance logs
@bot.event
async def on_guild_channel_delete(channel):  # channel delete logs
    logchannel = discord.utils.get(channel.guild.channels, name="maintenance")
    emb = discord.Embed(
        description=f"**#{channel.name} deleted in `{channel.category}`**",
        colour=0xC70600,
    )
    emb.set_author(name=f"{channel.guild}", icon_url=f"{channel.guild.icon_url}")
    emb.set_footer(text="Maintenance Log")
    await logchannel.send(embed=emb)


@bot.event
async def on_guild_channel_create(channel):  # channel create logs
    logchannel = discord.utils.get(channel.guild.channels, name="maintenance")
    emb = discord.Embed(
        description=f"**#{channel.name} created in `{channel.category}`**",
        colour=0xC70600,
    )
    emb.set_author(name=f"{channel.guild}", icon_url=f"{channel.guild.icon_url}")
    emb.set_footer(text="Maintenance Log")
    await logchannel.send(embed=emb)


# on message edit
@bot.event  # Working
async def on_message_edit(before, after):
    if (
        type(before.channel) == discord.channel.DMChannel
        or type(after.channel) == discord.channel.DMChannel
    ):
        return
    logchannel = discord.utils.get(before.guild.channels, name="message-logs")
    if before.content != after.content:
        message_content_before = discord.utils.escape_markdown(before.clean_content)
        if len(message_content_before)!=0:
            if message_content_before[-1]=='`':
                message_content_before = message_content_before + "\\"
        else:
            message_content_before = "None"
        message_content_after = discord.utils.escape_markdown(after.clean_content)
        if len(message_content_after)!=0:
            if message_content_after[-1]=='`':
                message_content_after = message_content_after + "\\"

        desc_before = message_content_before[:750]
        desc_after = message_content_after[:750]

        emb = discord.Embed(
            description=f"**Message edited in {before.channel.mention} at {after.edited_at}\n**\nMessage content Before\n```{desc_before}```Message content After\n```{desc_after}```[Jump to message]({after.jump_url})",
            colour=0xFF9C2E,
            timestamp=datetime.datetime.now(datetime.timezone.utc),
        )

        if len(message_content_before) > 750:
            emb.add_field(name='Message Content Before Continued',
                    value=f"```{message_content_before[750:]}```")

        if len(message_content_after) > 750:
            emb.add_field(name='Message Content After Continued',
                    value=f"```{message_content_after[750:]}```")

        emb.set_author(name=f"{before.author}", icon_url=f"{before.author.avatar_url}")
        emb.set_footer(text="Message Edit Log")
        await logchannel.send(embed=emb)
    else:
        pass



# on message delete
@bot.event  # Working
async def on_message_delete(message):
    if type(message.channel) == discord.channel.DMChannel:
        return
    logchannel = discord.utils.get(message.guild.channels, name="message-logs")

    content = discord.utils.escape_markdown(message.clean_content)
    if len(content)!=0:
        if content[-1] == '`':
            content = content+'\\'

    if (len(message.attachments)==0):
        emb = discord.Embed(
            description=f"**Message deleted in {message.channel.mention}**\n"
            f"Message Content\n```{content}```\n",
            colour=0xFF2E4A,
            timestamp=datetime.datetime.now(datetime.timezone.utc),
        )
        emb.add_field(name = "Message URL", value = f"{message.jump_url}", inline = False)
        emb.set_author(name=f"{message.author}", icon_url=f"{message.author.avatar_url}")
        emb.set_footer(text="Message Delete Log")
        await logchannel.send(embed=emb)
    else:
        for att in message.attachments:
            emb = discord.Embed(
                description=f"**Message deleted in {message.channel.mention}**\n"
                f"Text Content if any : \n```{content}```\n",
                colour=0xFF2E4A,
                timestamp=datetime.datetime.now(datetime.timezone.utc),
            )
            emb.add_field(name = "Message URL", value = f"{message.jump_url}", inline = False)
            async with aiohttp.ClientSession() as session:
                async with session.get(att.proxy_url) as resp:
                    if resp.status != 200:
                        return await logchannel.send('Could not log file...')
                    data = io.BytesIO(await resp.read())
                    img = discord.File(data, filename="logimages.png")
                    emb.set_image(url="attachment://logimages.png")
            emb.set_author(name=f"{message.author}", icon_url=f"{message.author.avatar_url}")
            emb.set_footer(text="Message Delete Log")
            await logchannel.send(file=img, embed=emb)


# On error Event
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(f"Usage: `{bot.command_prefix}{ctx.command.name} {ctx.command.usage}`")
        return

    if isinstance(error, commands.errors.MissingAnyRole):
        await ctx.send("User is not authorized to run this command.")
        return

    if isinstance(error, commands.errors.MemberNotFound):
        await ctx.send(error.args[0])
        return

    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            f"Invalid command. Please use `{bot.command_prefix}help` to list current valid commands."
        )
    else:
        embed = discord.Embed(
            title="Unhandled Exception Thrown in Command Invocation",
            color=0xFF0000,
            timestamp=datetime.datetime.now(datetime.timezone.utc),
        )

        exception_text = "".join(
            traceback.format_exception(type(error), error, error.__traceback__)
        )
        exception_text = exception_text[
            0 : exception_text.find("The above exception was")
        ].strip()

        print(exception_text, file=sys.stderr)

        try:
            chan_name = ctx.channel.name
        except:
            chan_name = "DMChannel"

        name = "Message Details:"
        value = f"```\nChannel: #{chan_name}\n"
        value += f"Author: {ctx.message.author}\n"
        value += f"Message: {ctx.message.content}\n```"

        embed.add_field(name=name, value=value, inline=False)

        field_len = 1000
        fields = [
            exception_text[i : i + field_len]
            for i in range(0, len(exception_text), field_len)
        ]

        for i, field in enumerate(fields):
            f_name = "Traceback:" if i == 0 else "Continued:"
            embed.add_field(name=f_name, value=f"```{field}```", inline=False)

        async with aiohttp.ClientSession() as s:
            webhook = discord.Webhook.from_url(
                f"https://discordapp.com/api/webhooks/{hookChannel}/{hookToken}",
                adapter=discord.AsyncWebhookAdapter(s),
            )
            await webhook.send(embed=embed)

        await ctx.send(
            f"An error occurred. Please use `{bot.command_prefix}reportbot <Error>`"
        )


# On error Event
@bot.event
async def on_error(event, *args, **kwargs):
    embed = discord.Embed(
        title="Unhandled Exception Thrown in Bot",
        color=0xFF0000,
        timestamp=datetime.datetime.now(datetime.timezone.utc),
    )

    exc_type, exc_value, exc_traceback = sys.exc_info()
    exception_text = "".join(
        traceback.format_exception(exc_type, exc_value, exc_traceback)
    )

    print(exception_text, file=sys.stderr)

    field_len = 1000
    fields = [
        exception_text[i : i + field_len]
        for i in range(0, len(exception_text), field_len)
    ]

    for i, field in enumerate(fields):
        f_name = "Traceback:" if i == 0 else "Continued:"
        embed.add_field(name=f_name, value=f"```{field}```", inline=False)

    async with aiohttp.ClientSession() as s:
        webhook = discord.Webhook.from_url(
            f"https://discordapp.com/api/webhooks/{hookChannel}/{hookToken}",
            adapter=discord.AsyncWebhookAdapter(s),
        )
        await webhook.send(embed=embed)


@bot.event
async def on_message(message):
    await bot.process_commands(message)


def poll_commands(cog) -> str:
    """
    Private function only to be called by the help command.
    Pulls the command info from cogs
    """
    commands = ""
    for cmd in cog.get_commands():
        if cmd.hidden:
            continue
        args = "" if not cmd.usage else f" {cmd.usage}"
        commands += f"`{bot.command_prefix}{cmd.name}{args}`"
        for alias in cmd.aliases:
            commands += f" | `{bot.command_prefix}{alias}{args}`"
        commands += f"\n{cmd.help}".rstrip("\n")
        commands += "\n\n"
    return commands


# JHDbot help message
@bot.command(name="help")  # alias of command name
async def _help(ctx, helprole=None):  # role-vise help section
    if type(ctx.channel) == discord.channel.DMChannel:
        await ctx.send('Bot does not respond to commands in DMs. Send your commands in the `#bot-commands` channel in JHDiscord.')
        return
    cool_people = discord.utils.get(ctx.author.roles, name="Moderator Emeritus")
    role = discord.utils.get(ctx.author.roles, name="Veteran")

    if (
        str(ctx.message.channel) == "bot-commands"
        or role is not None
        or cool_people is not None
        or ctx.message.author.guild_permissions.manage_messages
    ):

        header = ""
        footer = ""

        if not helprole:
            header = f"""
                Welcome to John hammond discord !\nHope you all have a fun time here, if you have some trouble reach out to our Admins or Moderators!
                **For moderators|veterans - {bot.command_prefix}help (moderator|veteran)**

                **General commands**
            """
            footer = "also feel free to drop a DM to any of our moderators/admins."

            cog = bot.cogs["GeneralCog"]
            commands = poll_commands(cog)

        elif helprole.lower() == "veteran":
            header = "**Veteran Commands**\n\n"
            footer = "**Also Every command a Member can use**"

            cog = bot.cogs["VeteranCog"]
            commands = poll_commands(cog)

        elif helprole.lower() == "moderator":
            header = "**Moderation Commands**\n\n"
            footer = "**Also every command a Veteran|Member can use**"

            cog = bot.cogs["ModeratorCog"]
            commands = poll_commands(cog)

        else:
            await ctx.send(
                f"`{helprole}` is not a valid option for `{bot.command_prefix}help`"
            )
            return

        embed = discord.Embed(description=header + commands + footer, colour=0xFF002A)
        await attach_embed_info(ctx, embed)
        await ctx.send(embed=embed)

    else:
        bot_commands = discord.utils.get(ctx.guild.channels, name="bot-commands")
        await ctx.send(f"Please use this command in {bot_commands.mention}")


async def attach_embed_info(ctx=None, embed=None):
    embed.set_author(name="JHDiscord Bot", icon_url=f"{ctx.guild.icon_url}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    embed.set_footer(text="by: JHD Moderation team ")
    return embed


if __name__ == "__main__":

    TOKEN = os.getenv("DISCORD_API_TOKEN")
    bot.run(TOKEN)  # token
