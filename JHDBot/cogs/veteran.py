#!/usr/bin/env python3
import asyncio
import urllib.request
import discord
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
        await ctx.message.delete()

    async def check_perms(self, ctx) -> bool:
        """
        Check permissions to make sure the user is allowed to issue commands
        """
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
        otw = discord.utils.get(ctx.guild.channels, name="over-the-wire")
        ctf = discord.utils.get(ctx.guild.channels, name="capture-the-flag")
        thm = discord.utils.get(ctx.guild.channels, name="tryhackme")
        big = discord.utils.get(ctx.guild.channels, name="beginners")
        htb = discord.utils.get(ctx.guild.channels, name="hackthebox")
        pro = discord.utils.get(ctx.guild.channels, name="programming")
        if await self.check_perms(ctx):
            await ctx.send(
                f"I. Bandit OverTheWire: (https://overthewire.org/wargames/bandit/) A wargame focusing on basic Linux "
                f"commands and privilege escalation. Questions can be asked in {otw.mention}\n\nII. Natas "
                f"OverTheWire: (https://overthewire.org/wargames/natas/) A wargame focusing on teaching the basics of "
                f"server side web-security. Questions can also be asked in the {otw.mention} channel.\n\nIII. "
                f"PicoCTF: (https://picoctf.com/) A very beginner CTF that is up year round for practice. Questions "
                f"can be asked in {ctf.mention} \n\nIV. Try Hack Me: (https://tryhackme.com/) A beginner friendly "
                f"platform focusing on learning how to hack in more real world situations than CTFs. There are "
                f'"rooms" for all levels and walkthroughs are available if necessary. Questions can be asked in '
                f'{thm.mention} also here is a guide, if you are starting with THM (https://blog.tryhackme.com/free_path/)\n\n'
                f'V. Hack the Box (https://www.hackthebox.eu/) Is a platform to learn and grow your pentesting skills.'
                f' Boxes range from "easy" to "insane" and cover a broad range of topics.'
                f' Walkthroughs can not be posted but "Starting point" will point you in the general direction.'
                f" Questions can also be asked in the {htb.mention} channel.\n\n"
                f"VI. Codecademy (https://www.codecademy.com) An interactive website for learning how to code. "
                f"This website teaches a variety of languages ranging from C++, to JavaScript in a very intuitive way. "
                f"Questions can be asked in the {pro.mention} channel.\n\n"
                f"For any additional questions or concerns, please consult the {big.mention} channel"
            )
        else:
            return

    # nypa command
    @commands.command(
        name="nypa", help="(Grey|Black) hat OSint auto message."
    )  # creating Commands ctx is something like context, send automatically
    async def not_your_personal_avengers(self, ctx):
        if await self.check_perms(ctx):
            await ctx.send(
                "We aren't your personal Avengers. You are going to need to use other methods for that. Customer "
                "support and local law enforcement are probably best depending on the circumstance."
            )
        else:
            return

    # blackhat command
    @commands.command(
        name="blackhat", aliases=["bt"], help="No blackhat auto message."
    )  # creating Commands ctx is something like context, send automatically
    async def black_hat(self, ctx):
        if await self.check_perms(ctx):
            channel = discord.utils.get(ctx.guild.channels, name="obligatory-rules")
            await ctx.send(
                f"Unfortunately it seems as though you are discussing blackhat activities. The term Blackhat refers "
                f"to hacking for personal gain or to be generally malicious. Please refer to {channel.mention} . We "
                f"do not and cannot support illegal or immoral activities as mentioned above."
            )
        else:
            return

    # account command
    @commands.command(
        name="account", aliases=["at"], help="Account recovery auto message."
    )  # creating Commands ctx is something like context, send automatically
    async def account(self, ctx):
        if await self.check_perms(ctx):
            await ctx.send(
                "Sorry. We can't help with account recovery. Your only path for that is to contact support for the "
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
                "CTF's are competitions you can participate into to practice and learn cybersecurity skills in a "
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
                "Hey there, if you ask the question like this, it might help us, to help you - "
                "https://www.youtube.com/watch?v=53zkBvL4ZB4 \n_LiveOverflow is dope_ : P"
            )
        else:
            return

    @commands.command(
        name="lmgtfy", help="Let me google that for you.", usage="<query>"
    )
    async def _lmgtfy(self, ctx, *, query=None):
        if await self.check_perms(ctx):
            if query is not None:
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
            if query is not None:
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
