import discord
from discord.ext import commands
import asyncio
import urllib


class VeteranCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # beginner command
    @commands.command(aliases=['bgn'])  # creating Commands ctx is something like context, send automatically
    async def beginner(self, ctx):
        cool_people = discord.utils.get(ctx.author.roles, name='Moderator Emeritus')
        otw = discord.utils.get(ctx.guild.channels, name='over-the-wire')
        ctf = discord.utils.get(ctx.guild.channels, name='capture-the-flag')
        thm = discord.utils.get(ctx.guild.channels, name='tryhackme')
        big = discord.utils.get(ctx.guild.channels, name='beginners')
        htb = discord.utils.get(ctx.guild.channels, name='hackthebox')
        role = discord.utils.get(ctx.author.roles, name='Veteran')
        if role is not None or cool_people is not None or ctx.message.author.guild_permissions.manage_messages:
            await ctx.send(
                f'I. Bandit OverTheWire: (https://overthewire.org/wargames/bandit/) A wargame focusing on basic Linux '
                f'commands and privilege escalation. Questions can be asked in {otw.mention}\n\nII. Natas '
                f'OverTheWire: (https://overthewire.org/wargames/natas/) A wargame focusing on teaching the basics of '
                f'server side web-security. Questions can also be asked in the {otw.mention} channel.\n\nIII. '
                f'PicoCTF: (https://picoctf.com/) A very beginner CTF that is up year round for practice. Questions '
                f'can be asked in {ctf.mention} \n\nIV. Try Hack Me: (https://tryhackme.com/) A beginner friendly '
                f'platform focusing on learning how to hack in more real world situations than CTFs. There are '
                f'"rooms" for all levels and walkthroughs are available if necessary. Questions can be asked in '
                f'{thm.mention} also here is a guide, if you are starting with THM (https://blog.tryhackme.com/going-from-zero-to-hero/)\n\n'
                f'V. Hack the Box (https://www.hackthebox.eu/) Is a platform to learn and grow your pentesting skills.'
                f' Boxes range from "easy" to "insane" and cover a broad range of topics.'
                f' Walkthroughs can not be posted but "Starting point" will point you in the general direction.'
                f' Questions can also be asked in the {htb.mention} channel.\n\n'
                f'For any additional questions or concerns, please consult the {big.mention} channel')
        else:
            await ctx.send('Seems like you are not authorized to use this command.')
        await asyncio.sleep(5)
        await ctx.message.delete()

    # nypa command
    @commands.command(aliases=['nypa'])  # creating Commands ctx is something like context, send automatically
    async def not_your_personal_avengers(self, ctx):
        cool_people = discord.utils.get(ctx.author.roles, name="Moderator Emeritus")
        role = discord.utils.get(ctx.author.roles, name="Veteran")
        if role is not None or cool_people is not None or ctx.message.author.guild_permissions.manage_messages:
            await ctx.send(
                'We aren\'t your personal Avengers. You are going to need to use other methods for that. Customer '
                'support and local law enforcement are probably best depending on the circumstance.')
        else:
            await ctx.send('Seems like you are not authorized to use this command D:')
        await asyncio.sleep(5)
        await ctx.message.delete()

    # blackhat command
    @commands.command(aliases=['bt','blackhat'])  # creating Commands ctx is something like context, send automatically
    async def black_hat(self, ctx):
        role = discord.utils.get(ctx.author.roles, name='Veteran')
        cool_people = discord.utils.get(ctx.author.roles, name='Moderator Emeritus')
        channel = discord.utils.get(ctx.guild.channels, name='obligatory-rules')
        if role is not None or cool_people is not None or ctx.message.author.guild_permissions.manage_messages:
            await ctx.send(
                f'Unfortunately it seems as though you are discussing blackhat activities. The term Blackhat refers '
                f'to hacking for personal gain or to be generally malicious. Please refer to {channel.mention} . We '
                f'do not and cannot support illegal or immoral activities as mentioned above.')
        else:
            await ctx.send('Seems like you are not authorized to use this command.')
        await asyncio.sleep(5)
        await ctx.message.delete()

    # account command
    @commands.command(aliases=['at'])  # creating Commands ctx is something like context, send automatically
    async def account(self, ctx):
        role = discord.utils.get(ctx.author.roles, name='Veteran')
        cool_people = discord.utils.get(ctx.author.roles, name='Moderator Emeritus')
        if role is not None or cool_people is not None or ctx.message.author.guild_permissions.manage_messages:
            await ctx.send(
                'Sorry. We can\'t help with account recovery. Your only path for that is to contact support for the '
                'respective service. "I forgot my password" is often a good place to start.')
        else:
            await ctx.send('Seems like you are not authorized to use this command D:')
        await asyncio.sleep(5)
        await ctx.message.delete()

    # just ask it mate
    @commands.command(aliases=['ja', 'justask'])  # creating Commands ctx is something like context, send automatically
    async def just_ask(self, ctx):
        role = discord.utils.get(ctx.author.roles, name='Veteran')
        cool_people = discord.utils.get(ctx.author.roles, name='Moderator Emeritus')
        if role is not None or cool_people is not None or ctx.message.author.guild_permissions.manage_messages:
            await ctx.send(
                'Please don\'t ask to ask a question, ask if anyone is on, or ask for an expert. Just ask your '
                'question. That is the only way to get an answer.')
        else:
            await ctx.send('Seems like you are not authorized to use this command D:')
        await asyncio.sleep(5)
        await ctx.message.delete()

    # ctfwhat command
    @commands.command(aliases=['ct', 'ctfwhat'])  # creating Commands ctx is something like context, send automatically
    async def ctf_what(self, ctx):
        role = discord.utils.get(ctx.author.roles, name='Veteran')
        cool_people = discord.utils.get(ctx.author.roles, name='Moderator Emeritus')
        if role is not None or cool_people is not None or ctx.message.author.guild_permissions.manage_messages:
            await ctx.send(
                'CTF\'s are competitions you can participate into to practice and learn cybersecurity skills in a '
                'legal way. Here is a pretty cool video that explains them. '
                'https://www.youtube.com/watch?v=8ev9ZX9J45A&t=2s \n\nWargames are similar but run all the time where '
                'as CTFs tend to just run for a few days.')
        else:
            await ctx.send('Seems like you are not authorized to use this command D:')
        await asyncio.sleep(5)
        await ctx.message.delete()

    # howtoask command
    @commands.command(aliases=['hk', 'howtoask'])  # creating Commands ctx is something like context, send automatically
    async def how_to_ask(self, ctx):
        role = discord.utils.get(ctx.author.roles, name='Veteran')
        cool_people = discord.utils.get(ctx.author.roles, name='Moderator Emeritus')
        if role is not None or cool_people is not None or ctx.message.author.guild_permissions.manage_messages:
            await ctx.send(
                'Hey there, if you ask the question like this, it might help us, to help you - '
                'https://www.youtube.com/watch?v=53zkBvL4ZB4 \n_LiveOverflow is dope_ : P')
        else:
            await ctx.send('Seems like you are not authorized to use this command D:')
        await asyncio.sleep(5)
        await ctx.message.delete()

    @commands.command(aliases=['lmgtfy'])
    async def _lmgtfy(self, ctx, *, input):
        role = discord.utils.get(ctx.author.roles, name='Veteran')
        cool_people = discord.utils.get(ctx.author.roles, name='Moderator Emeritus')
        if role is not None or cool_people is not None or ctx.message.author.guild_permissions.manage_messages:
            lmgtfyurl = 'https://lmgtfy.com/?q='
            fullyurl = lmgtfyurl + urllib.parse.quote_plus(input, safe='')
            await ctx.send(fullyurl)
        else:
            await ctx.send('Seems like you are not authorized to use this command D:')
        await asyncio.sleep(5)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(VeteranCog(bot))
    print('Veteran cog loaded')
