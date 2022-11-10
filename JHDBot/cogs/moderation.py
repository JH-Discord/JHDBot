#!/usr/bin/env python3
import asyncio
import csv
import random
import discord
import os
import pathlib
from discord.ext import commands


class ModeratorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Clear Message Command..
    @commands.command(
        name="clear", help="Deletes messages", usage="[number of messages to delete]"
    )
    async def clear(
        self, ctx, amount=2
    ):  # amount=2 sets the default value to 2 basically command + the text above that
        try:
            if ctx.message.author.guild_permissions.manage_messages:
                if amount <= 20:
                    await ctx.channel.purge(
                        limit=amount + 1
                    )  # limit= number of messages going to be deleted !
                    msg = await ctx.channel.send(f"Deleted {amount} messages D:")
                else:
                    await ctx.channel.send(
                        "Sorry, max 20 messages can be deleted at a time"
                    )
            else:
                msg = await ctx.send(
                    "Sorry, it seems like you are not authorized to do it"
                )
            await asyncio.sleep(5)
            await msg.delete()
        except:
            await ctx.send("The bot is unauthorized to delete messages D:")

    # Mute Command..
    @commands.command(
        name="mute",
        help="Mutes a specified user for some time.",
        usage="[user mention or id] [time in seconds]",
    )  # a function to mute members
    async def mute(
        self, ctx, user: discord.Member, seconds=None
    ):  # gets context user and time(in seconds), default being None
        try:
            if ctx.message.author.guild_permissions.kick_members:
                if seconds is None or int(seconds) < 0:
                    # if no time supplied, function exits
                    await ctx.send(
                        "Please also supply time in seconds (proper +ve int format plz)."
                    )
                    return
                else:
                    # check perms. if user has perms to manage message like if he mod he can't be muted by the bot.
                    if user.guild_permissions.manage_messages:
                        await ctx.send(f"Sorry, can't mute {user} because of perms : (")
                        return
                    # add mute role
                    role = discord.utils.get(ctx.guild.roles, name="Muted")
                    muted_role = discord.utils.get(ctx.guild.roles, name="Member")
                    await user.add_roles(role)
                    await user.remove_roles(muted_role)
                    await user.send(
                        f"You were muted in JHDiscord for `{seconds}` seconds"
                    )
                    await ctx.send(
                        f"{user} has been muted in JHD for `{seconds}` seconds"
                    )
                    muted = discord.utils.get(user.roles, name="Muted")
                    if muted is not None:
                        await asyncio.sleep(int(seconds))
                        await user.remove_roles(role)
                        await user.add_roles(muted_role)
                        await user.send(
                            "You were un-muted in JHDiscord, we hope you don't repeat the actions that lead the "
                            "mod/admin to mute you."
                        )
                        await ctx.send(f"{user} has been unmuted in JHD")
            else:
                await ctx.send("Sorry, it seems like you are not authorized to do it")
        except:
            await ctx.send("Seems like the bot is not authorized to run this command")

    # unmute command..
    @commands.command(
        name="unmute", help="Unmutes a specified user.", usage="[user mention or id]"
    )
    async def unmute(self, ctx, user: discord.Member):
        try:
            if ctx.message.author.guild_permissions.kick_members:
                muted = discord.utils.get(user.roles, name="Muted")
                if muted is not None:
                    role = discord.utils.get(ctx.guild.roles, name="Muted")
                    mrole = discord.utils.get(ctx.guild.roles, name="Member")
                    await user.remove_roles(role)
                    await user.add_roles(mrole)
                    await user.send(
                        "You were un-muted in JHDiscord, we hope you don't repeat the actions that lead the "
                        "mod/admin to mute you."
                    )
                    await ctx.send(f"{user} has been unmuted in JHD")
                else:
                    await ctx.send(f"{user} is not muted ¯\_(ツ)_/¯ ")
            else:
                await ctx.send("Sorry, it seems like you are not authorized to do it")
            await asyncio.sleep(5)
            await ctx.message.delete()
        except:
            await ctx.send("Seems like the Bot is not authorized to run this command")

    @commands.command(
        name="kick",
        help="Kicks a specified user.",
        usage="[user mention or id] [reason]",
    )
    @commands.has_permissions(kick_members=True)
    @commands.has_any_role("Admin", "Moderator")
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        if user.guild_permissions.manage_messages:
            # check perms. if user has perms to manage message like if he mod he can't be banned by the bot.
            await ctx.send(
                f"Sorry. As much as I too would like to kick {user}, NightWolf wouldn't like that :("
            )
        elif ctx.message.author.guild_permissions.ban_members:
            kickgifs_path = pathlib.Path(os.environ["GIFDIR"] + "/kick.csv")
            kick_gifs = []
            if kickgifs_path.exists():
                with open(kickgifs_path, "r") as f:
                    kick_gifs = list(csv.reader(f))[0]
            else:
                # Just use a generic kick gif if the file is not found
                kick_gifs = [
                    "https://tenor.com/view/kick-knock-out-hurt-ouch-gif-4799973"
                ]

            gif = random.choice(kick_gifs)

            await ctx.guild.kick(user=user, reason=reason)  # kick the user
            await ctx.send(f"{user} has been kicked from the server")
            await ctx.send(gif)

            # This could throw an exception if the user does not allow DMs
            try:
                # Sends a DM letting the user know they were banned
                await user.send(f"You were kicked from JHDiscord : {reason}")
                await user.send(gif)
            except:
                pass

        else:
            await ctx.send(
                "Sorry, it seems like you are not authorized to kick members"
            )
        await asyncio.sleep(5)
        await ctx.message.delete()

    # Ban Member Command..
    @commands.command(
        name="ban", help="Bans a specified user.", usage="[user mention or id] [reason]"
    )  # a function to ban members
    async def ban(
        self, ctx, user: discord.Member, *, reason=None
    ):  # gets context user and reason, default being None
        if user.guild_permissions.manage_messages:
            # check perms. if user has perms to manage message like if he mod he can't be banned by the bot.
            await ctx.send(
                f"Sorry. As much as I too would like to ban {user}, NightWolf wouldn't like that :("
            )
        elif ctx.message.author.guild_permissions.ban_members:
            bangifs_path = pathlib.Path(os.environ["GIFDIR"] + "/ban.csv")
            ban_gifs = []
            if bangifs_path.exists():
                with open(bangifs_path, "r") as f:
                    ban_gifs = list(csv.reader(f))[0]
            else:
                # Just use a generic ban gif if the file is not found
                ban_gifs = [
                    "https://tenor.com/view/blob-banned-ban-hammer-blob-ban-emoji-gif-16021044"
                ]

            gif = random.choice(ban_gifs)

            await ctx.guild.ban(user=user, reason=reason)  # ban the user
            await ctx.send(f"{user} has been banned from the server")
            await ctx.send(gif)

            # This could throw an exception if the user does not allow DMs
            try:
                # Sends a DM letting the user know they were banned
                await user.send(f"You were banned from JHDiscord : {reason}")
                await user.send(gif)
            except:
                pass

        else:
            await ctx.send("Sorry, it seems like you are not authorized to ban members")
        await asyncio.sleep(5)
        await ctx.message.delete()

    # MultiKick Member Command..
    @commands.command(name="multikick", hidden=True)  # a function to multikick members
    async def multikick(self, ctx, *, users):  # gets user ids in string.
        try:
            if ctx.message.author.guild_permissions.kick_members:
                listofusers = users.split()
                reason = "Kicked during a multikick process. Most probably we suspect you to be a bot. If you are not please rejoin later."
                for i in listofusers:
                    user = await self.bot.fetch_user(i[3:-1])
                    try:
                        await user.send(f"You were kicked from JHDiscord : {reason}")
                        await ctx.guild.kick(
                            user=user, reason=reason
                        )  # kicks that user
                        await ctx.send(f"{user} has been kicked out from the server")
                    except:
                        await ctx.send(
                            "Can't kick the user because of their permissions, though they might have gotten a kick message."
                        )
            else:
                await ctx.send("Sorry, it seems like you are not authorized to do it")
            await asyncio.sleep(5)
            await ctx.message.delete()
        except:
            await ctx.send("The bot is unauthorized to kick members.")

    # Multiban Member Command..
    @commands.command(name="multiban", hidden=True)  # a function to multiban members
    async def multiban(self, ctx, *, users):  # gets user id in string.
        try:
            if ctx.message.author.guild_permissions.kick_members:
                listofusers = users.split()
                reason = "Banned during a multiban process. Most probably we are sure that you are a bot. If you aren't: You'd make an excellent bot! :) Please reach out to our staff on other servers, like THM, HTB, yada yada."
                for i in listofusers:
                    user = await self.bot.fetch_user(i[3:-1])
                    try:
                        await user.send(f"You were banned from JHDiscord : {reason}")
                        await ctx.guild.ban(user=user, reason=reason)  # bans that user
                        await ctx.send(f"{user} has been banned out from the server")
                    except:
                        await ctx.send(
                            "Can't ban the user because of their permissions, though they might have gotten a ban message."
                        )
            else:
                await ctx.send("Sorry, it seems like you are not authorized to do it")
            await asyncio.sleep(5)
            await ctx.message.delete()
        except:
            await ctx.send("The bot is unauthorized to ban members.")

    @commands.command(
        name="addgif", help="Adds a ban/kick gif", usage="[kick/ban] [url to gif]"
    )
    @commands.has_permissions(kick_members=True)
    @commands.has_any_role("Admin", "Moderator")
    async def addgif(self, ctx, option, *, url: str = None):
        if url is None:
            await ctx.send(
                f"Usage: `{self.bot.command_prefix}{ctx.command.name} "
                f"{ctx.command.usage}`"
            )
            return

        filename = ""
        if option.lower() == "kick":
            filename = os.environ["GIFDIR"] + "/kick.csv"
        elif option.lower() == "ban":
            filename = os.environ["GIFDIR"] + "/ban.csv"
        else:
            await ctx.send(
                f"Usage: `{self.bot.command_prefix}{ctx.command.name} "
                f"{ctx.command.usage}`"
            )
            return

        url.strip("\n")
        if url[-1] == "/":
            url = url.rstrip("/")

        with open(filename, "r") as f:
            gifs = list(csv.reader(f))[0]
            if url in gifs:
                await ctx.send("Gif already added.")
                return

        gifs.append(url)
        with open(filename, "w") as f:
            writer = csv.writer(f)
            writer.writerow(gifs)

        await ctx.send(f"Gif: `{url}` added.")
        return

    @commands.command(
        name="removegif",
        aliases=["rmgif"],
        help="Removes a ban/kick gif",
        usage="[kick/ban] [url to gif]",
    )
    @commands.has_permissions(kick_members=True)
    @commands.has_any_role("Admin", "Moderator")
    async def removegif(self, ctx, option, *, url: str = None):
        if url is None:
            await ctx.send(
                f"Usage: `{self.bot.command_prefix}{ctx.command.name} "
                f"{ctx.command.usage}`"
            )
            return

        filename = ""
        if option.lower() == "kick":
            filename = os.environ["GIFDIR"] + "/kick.csv"
        elif option.lower() == "ban":
            filename = os.environ["GIFDIR"] + "/ban.csv"
        else:
            await ctx.send(
                f"Usage: `{self.bot.command_prefix}{ctx.command.name} "
                f"{ctx.command.usage}`"
            )
            return

        url.strip("\n")
        if url[-1] == "/":
            url = url.rstrip("/")

        with open(filename, "r") as f:
            gifs = list(csv.reader(f))[0]

        if url not in gifs:
            await ctx.send(f"Gif `{url}` not in `{option.lower()}` database.")
            return

        gifs.remove(url)

        with open(filename, "w") as f:
            writer = csv.writer(f)
            writer.writerow(gifs)

        await ctx.send(f"Gif: `{url}` removed.")
        return

    @commands.command(
        name="listgifs",
        aliases=["lsgifs"],
        help="List gifs in database",
        usage="[kick/ban]",
    )
    @commands.has_permissions(kick_members=True)
    @commands.has_any_role("Admin", "Moderator")
    async def listgifs(self, ctx, option):
        filename = ""
        if option.lower() == "kick":
            filename = os.environ["GIFDIR"] + "/kick.csv"
        elif option.lower() == "ban":
            filename = os.environ["GIFDIR"] + "/ban.csv"
        else:
            await ctx.send(
                f"Usage: `{self.bot.command_prefix}{ctx.command.name} "
                f"{ctx.command.usage}`"
            )
            return

        with open(filename, "r") as f:
            gifs = list(csv.reader(f))[0]

        gifs = "\n".join(gifs)
        await ctx.send(f"{option} gifs:\n```\n{gifs}\n```")
        return


def setup(bot):
    bot.add_cog(ModeratorCog(bot))
    print("Moderation cog loaded")
