#!/usr/bin/env python3
import aiohttp
import asyncio
import discord
import inspect
import json
import os
import urllib.request
from discord.ext import commands


class VeteranCog(commands.Cog):
    def __init__(self, bot):
        self.name = "veteran"
        self.bot = bot

    async def cog_after_invoke(self, ctx: commands.Context) -> None:
        """
        Clean up messages that trigger the command after it's invoked
        """
        await asyncio.sleep(5)
        try:
            await ctx.message.delete()
        except:
            pass

    async def check_perms(self, ctx) -> bool:
        """
        Check permissions to make sure the user is allowed to issue commands
        """
        if type(ctx.channel) == discord.channel.DMChannel:
            await ctx.send('The bot does not respond to commands in DMs. Send your commands in the `#'+os.getenv("BOT_COMMAND_CHANNEL")+'` channel in JHDiscord.')
            return

        cool_people = discord.utils.get(ctx.author.roles, name="Moderator Emeritus")
        role = discord.utils.get(ctx.author.roles, name="Veteran")
        if (
            role is not None
            or cool_people is not None
            or ctx.message.author.guild_permissions.manage_messages
        ):
            return True
        else:
            await ctx.send("Seems like you are not authorized to use this command D:")
            await asyncio.sleep(5)
            await ctx.message.delete()
            return False

    # beginner command
    @commands.command(
        name="beginner", aliases=["bgn"], help="Beginner help message."
    )  # creating Commands ctx is something like context, send automatically
    async def beginner(self, ctx):
        if await self.check_perms(ctx):
            wargames_channel = discord.utils.get(ctx.guild.channels, name=os.getenv("WARGAMES"))
            ctfchat_channel = discord.utils.get(ctx.guild.channels, name=os.getenv("CTF_CHAT"))
            beginner_channel = discord.utils.get(ctx.guild.channels, name=os.getenv("BEGINNERS"))
            programming_channel = discord.utils.get(ctx.guild.channels, name=os.getenv("PROGRAMMING"))

            beginner_message = f"""
            I. OverTheWire: (<https://overthewire.org/wargames/>): Collection of wargames designed for learning about security and CTFs. Discussion about OverTheWire can be done in {wargames_channel.mention}.

            II. PicoCTF: (<https://picoctf.com/>): A super beginner-friendly CTF that is up year round for practice. You can chat about PicoCTF in {ctfchat_channel.mention}.

            III. TryHackMe: (<https://tryhackme.com/>): A beginner friendly platform focusing on learning how to hack in more real-world situations than CTFs. There are so-called "rooms" for all levels and walkthroughs available if necessary. Questions can be asked in {wargames_channel.mention}. Also here is a guide, if you are starting with THM (<https://blog.tryhackme.com/free_path/>)

            IV. Hack the Box (<https://www.hackthebox.eu/>): A platform to learn and grow your pentesting skills. Boxes range from "easy" to "insane" and cover a broad range of topics. Walkthroughs cannot be posted but "Starting point" (<https://app.hackthebox.eu/starting-point>) will point you in the general direction. HTB Academy (<https://academy.hackthebox.eu/>) is another excellent resource. The {wargames_channel.mention} channel can be used for discussing Hack the Box content.

            V. Codecademy (<https://www.codecademy.com>): An interactive website for learning how to code. This website teaches a variety of languages ranging from C++ to JavaScript in a very intuitive way. Questions can be asked in the {programming_channel.mention} channel.

            For any additional questions or concerns, please consult the {beginner_channel.mention} channel.
            """

            await ctx.send(inspect.cleandoc(beginner_message))
        else:
            return

    # nypa command
    @commands.command(
        name="nypa", help="(Grey|Black) hat OSINT auto message."
    )  # creating Commands ctx is something like context, send automatically
    async def not_your_personal_avengers(self, ctx):
        if await self.check_perms(ctx):
            await ctx.send(
                "We aren't your personal Avengers. You are going to need to use other methods for that: Customer "
                "support and local law enforcement are probably best depending on the circumstance."
            )
        else:
            return

    # Cat command - to embed wholesomeness in chat
    @commands.command(
        name="cat",
        help="Command to add wholesomeness to chat."
    )
    async def cat(self, ctx):
        if await self.check_perms(ctx):
            async with aiohttp.ClientSession() as session:
                async with session.get('https://api.thecatapi.com/api/images/get?format=json') as response:
                    html = json.loads(await response.text())
                    emb = discord.Embed(description=f'Kato <3', colour=0x3CFF4C)
                    emb.set_footer(text=f"Cute isn't it/kawai deso ?")
                    emb.set_image(url=(html[0]["url"]))
                    await ctx.send(embed=emb)
        else:
            return

    # blackhat command
    @commands.command(
        name="blackhat",
        aliases=[
          "bt",
          "bh"
        ],
        help="No blackhat auto message."
    )  # creating Commands ctx is something like context, send automatically
    async def black_hat(self, ctx):
        if await self.check_perms(ctx):
            channel = discord.utils.get(ctx.guild.channels, name=os.getenv("RULES_CHANNEL"))
            await ctx.send(
                f"Unfortunately it seems as though you are discussing blackhat activities. The term Blackhat refers "
                f"to hacking for personal gain or to be generally malicious. Please refer to {channel.mention} . We "
                f"do not and cannot support illegal or immoral activities as mentioned above."
            )
        else:
            return

    # blackhat doge meme
    @commands.command(
        name="noblackhat",
        aliases=[
          "nbt",
          "nbh"
        ],
        help="No blackhat but with a meme."
    )
    async def no_black_hat(self, ctx):
        if await self.check_perms(ctx):
            await ctx.send(
                "https://cdn.discordapp.com/attachments/701793795749970042/824043387291828234/bt.jpg"
            )
        return

    # account command
    @commands.command(
        name="account", aliases=["at"], help="Account recovery auto message."
    )  # creating Commands ctx is something like context, send automatically
    async def account(self, ctx):
        if await self.check_perms(ctx):
            await ctx.send(
                "Sorry. We can't help with account recovery. Your only option is to contact support for the "
                'respective service. "I forgot my password" is often a good place to start.'
            )
        else:
            return

    # just ask it mate
    @commands.command(
        name="justask",
        aliases=["ja"],
        help="When someone asks to ask a question or asks if someone is online.",
    )  # creating Commands ctx is something like context, send automatically
    async def just_ask(self, ctx):
        if await self.check_perms(ctx):
            await ctx.send(
                "Please don't ask to ask a question, ask if anyone is on, or ask for an expert. Just ask your "
                "question. That is the only way to get an answer."
            )
        else:
            return

    # ctfwhat command
    @commands.command(
        name="ctfwhat", aliases=["ctf"], help="What is CTF auto message."
    )  # creating Commands ctx is something like context, send automatically
    async def ctf_what(self, ctx):
        if await self.check_perms(ctx):
            await ctx.send(
                "CTFs are competitions you can participate in to practice and learn cybersecurity skills in a "
                "legal way. Here is a pretty cool video that explains them. "
                "https://www.youtube.com/watch?v=8ev9ZX9J45A&t=2s \n\nWargames are similar but run all the time where "
                "as CTFs tend to just run for a few days."
            )
        else:
            return

    # howtoask command
    @commands.command(
        name="howtoask", aliases=["hk"], help="LO video on how to ask a question."
    )  # creating Commands ctx is something like context, send automatically
    async def how_to_ask(self, ctx):
        if await self.check_perms(ctx):
            await ctx.send(
                "Hey there, if you ask the question like this, it will help us helping you - "
                "https://www.youtube.com/watch?v=53zkBvL4ZB4 \n_LiveOverflow is dope_ : P"
            )
        else:
            return

    @commands.command(
        name="lmgtfy", help="Let me google that for you.", usage="<query>"
    )
    async def _lmgtfy(self, ctx, *, query=None):
        if await self.check_perms(ctx):
            if query is None:
                await ctx.send(
                    f"Query not provided: `{self.bot.command_prefix}lmgtfy <query>`"
                )
            else:
                lmgtfyurl = "https://lmgtfy.com/?q="
                fullyurl = lmgtfyurl + urllib.parse.quote_plus(query, safe="")
                await ctx.send(fullyurl)
        else:
            return

    # google command
    @commands.command(
        name="google", aliases=["gs"], help="Google something.", usage="<query>"
    )
    async def google(self, ctx, *, query=None):
        if await self.check_perms(ctx):
            if query is None:
                await ctx.send(
                    f"Query not provided: `{self.bot.command_prefix}gs <query>`"
                )
            else:
                googleurl = "https://www.google.com/search?safe=active&q="
                fullurl = googleurl + urllib.parse.quote_plus(query, safe="")
                await ctx.send(fullurl)
        else:
            return


def setup(bot):
    bot.add_cog(VeteranCog(bot))
    print("Veteran cog loaded")
