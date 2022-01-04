#!/usr/bin/env python3
import discord
from discord.ext import commands
import strings


class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.name = "general"
        self.bot = bot

    async def pre_invoke(self, ctx) -> bool:
        if type(ctx.channel) == discord.channel.DMChannel:
            await ctx.send('Bot does not respond to commands in DMs. Send your commands in the `#bot-commands` channel in JHDiscord.')
            return False
        else:
            return True

    # Ping Command to check if server is up or not
    @commands.command(
        name="ping", help="Command to check if bot is online and latency."
    )
    # creating Commands ctx is something like context, send automatically
    async def ping(self, ctx):
        if await self.pre_invoke(ctx):
            role = discord.utils.get(ctx.author.roles, name="Veteran")
            cool_people = discord.utils.get(ctx.author.roles, name="Moderator Emeritus")
            if (
                str(ctx.message.channel) == "bot-commands"
                or role is not None
                or cool_people is not None
                or ctx.message.author.guild_permissions.manage_messages
            ):
                await ctx.send(f"Ping! - {round(self.bot.latency * 1000)}ms")
            else:
                await ctx.send("Please use this command in `#bot-commands`")

    # For Likt
    @commands.command(name="solve", hidden=True)
    async def solve(self, ctx):
        if await self.pre_invoke(ctx):
            role = discord.utils.get(ctx.author.roles, name="Veteran")
            cool_people = discord.utils.get(ctx.author.roles, name="Moderator Emeritus")
            if (
                str(ctx.message.channel) == "bot-commands"
                or role is not None
                or cool_people is not None
                or ctx.message.author.guild_permissions.manage_messages
            ):
                await ctx.send("That is a definite maybe")
            else:
                await ctx.send("Please use this command in `#bot-commands`")

    # Report bot command
    @commands.command(
        name="reportbot",
        help="You can use this command to report any issue with JHD_Bot or new suggestions.",
        usage="<issue>",
    )
    async def report_bot(self, ctx, *, reason=None):
        if await self.pre_invoke(ctx):
            coolpeople = discord.utils.get(ctx.author.roles, name="Moderator Emeritus")
            if (
                str(ctx.message.channel) == "bot-commands"
                or coolpeople is not None
                or ctx.message.author.guild_permissions.manage_messages
            ):
                if reason is None:
                    await ctx.send("Invalid syntax, please add the issue you are facing.")
                else:
                    channel = discord.utils.get(
                        ctx.message.author.guild.channels, name="dev-team"
                    )
                    await channel.send(f"Reported by user {ctx.message.author} : " + reason)
                    await ctx.send(
                        "Your report has been successfully forwarded to moderators"
                    )
            else:
                await ctx.send("Please use this command in `#bot-commands`")

    # reporting users
    @commands.command(
        name="report",
        help="You can use this command to report against a user, you need to tag user and give the reason, please don't use this command as some play thing.",
        usage="[user] [reason]",
    )
    async def report(self, ctx, user=None, *, reason=None):
        if await self.pre_invoke(ctx):
            cool_people = discord.utils.get(ctx.author.roles, name="Moderator Emeritus")
            if (
                str(ctx.message.channel) == "bot-commands"
                or cool_people is not None
                or ctx.message.author.guild_permissions.manage_messages
            ):
                if reason is None or user is None:
                    await ctx.send(
                        f"Invalid syntax, please check `{self.bot.command_prefix}help` to check the syntax and "
                        f"pass proper arguments."
                    )
                else:
                    channel = discord.utils.get(
                        ctx.message.author.guild.channels, name="moderators"
                    )
                    await channel.send(
                        f"Reported by user {ctx.message.author} : Complain against user {user} - "
                        + reason
                    )
                    await ctx.send(
                        "Your report has been successfully forwarded to moderators"
                    )
            else:
                await ctx.send("Please use this command in `#bot-commands`")

    # Suggestion command
    @commands.command(
        name="suggest",
        help="To submit a suggestion for JHD server.",
        usage="<suggestion>",
    )
    async def suggest(self, ctx, *, sug=None):
        if await self.pre_invoke(ctx):
            cool_people = discord.utils.get(ctx.author.roles, name="Moderator Emeritus")
            if (
                str(ctx.message.channel) == "bot-commands"
                or cool_people is not None
                or ctx.message.author.guild_permissions.manage_messages
            ):
                if sug is None:
                    await ctx.send("oops, seems like you forgot to add the suggestion .")
                else:
                    channel = discord.utils.get(
                        ctx.message.author.guild.channels, name="suggestions"
                    )
                    emb = discord.Embed(description=sug, colour=0xFF002A)
                    emb.set_author(
                        name=f"{ctx.message.author}",
                        icon_url=f"{ctx.message.author.avatar_url}",
                    )
                    emb.set_footer(
                        text=f"Submit your suggestions using: "
                        f"{self.bot.command_prefix}suggest <suggestion> in #bot-commands"
                    )
                    msg = await channel.send(embed=emb)
                    await msg.add_reaction("👍")
                    await msg.add_reaction("👎")
                    await ctx.send(f"Your suggestion has been added in {channel.mention}")
            else:
                await ctx.send("Please use this command in `#bot-commands`")

    # Channel desc message
    @commands.command(
        name="chdesc",
        aliases=["channeldesc"],
        help="Give the description of all channels.",
    )
    async def channel_desc(self, ctx):
        if await self.pre_invoke(ctx):
            role = discord.utils.get(ctx.author.roles, name="Veteran")
            coolpeople = discord.utils.get(ctx.author.roles, name="Moderator Emeritus")
            if (
                str(ctx.message.channel) == "bot-commands"
                or role is not None
                or coolpeople is not None
                or ctx.message.author.guild_permissions.manage_messages
            ):

                emb = discord.Embed(description=strings.channels, colour=0xFF002A)
                await self.attach_embed_info(ctx, emb)
                await ctx.message.author.send(embed=emb)
                emb = discord.Embed(description=strings.channels2, colour=0xFF002A)
                await self.attach_embed_info(ctx, emb)
                await ctx.message.author.send(embed=emb)
            else:
                await ctx.send("Please use this command in `#bot-commands`")

    # FAQ message
    @commands.command(
        name="FAQ", aliases=["qna"], help="The list of frequently asked questions."
    )
    async def faq(self, ctx):
        if await self.pre_invoke(ctx):
            role = discord.utils.get(ctx.author.roles, name="Veteran")
            coolpeople = discord.utils.get(ctx.author.roles, name="Moderator Emeritus")
            if (
                str(ctx.message.channel) == "bot-commands"
                or role is not None
                or coolpeople is not None
                or ctx.message.author.guild_permissions.manage_messages
            ):
                emb = discord.Embed(description=strings.faq, colour=0xFF002A)
                await self.attach_embed_info(ctx, emb)
                await ctx.send(embed=emb)
            else:
                await ctx.send("Please use this command in `#bot-commands`")

    async def attach_embed_info(self, ctx=None, embed=None):
        embed.set_author(name="JHDiscord Bot", icon_url=f"{ctx.guild.icon_url}")
        embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
        embed.set_footer(text="by: JHD Moderation team ")
        return embed

    # Send github link
    @commands.command(
        name="source", help="JHDBot github link."
    )
    async def source(self, ctx):
        if await self.pre_invoke(ctx):
            if (
                str(ctx.message.channel) == "bot-commands"
            ):
                # 0x979C9F == light grey
                emb = discord.Embed(description=strings.url, colour=0x979C9F)
                await self.attach_embed_info(ctx, emb)
                await ctx.send(embed=emb)
            else:
                await ctx.send("Please use this command in `#bot-commands`")

def setup(bot):
    bot.add_cog(GeneralCog(bot))
    print("General cog loaded")
