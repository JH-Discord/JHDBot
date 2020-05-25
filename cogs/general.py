import discord
from discord.ext import commands
import asyncio


class GeneralCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Ping Command to check if server is up or not
    @commands.command()
    # creating Commands ctx is something like context, send automatically
    async def ping(self, ctx):
        role = discord.utils.get(ctx.author.roles, name='Veteran')
        cool_people = discord.utils.get(ctx.author.roles, name='Cool People')
        if (str(
                ctx.message.channel) == "bot-commands" or role is not None or cool_people is not None
                or ctx.message.author.guild_permissions.manage_messages):
            await ctx.send(f'Ping - {round(self.bot.latency * 1000)}ms')
        else:
            await ctx.send('Please use this command in `#bot-commands`')

    # For Likt
    @commands.command()
    async def solve(self, ctx, *, input=None):
        role = discord.utils.get(ctx.author.roles, name='Veteran')
        cool_people = discord.utils.get(ctx.author.roles, name='Cool People')
        if (str(
                ctx.message.channel) == "bot-commands" or role is not None or cool_people is not None
                or ctx.message.author.guild_permissions.manage_messages):
            await ctx.send("That is a definite maybe")
        else:
            await ctx.send("Please use this command in `#bot-commands`")

    # Report bot command
    @commands.command()
    async def report_bot(self, ctx, *, reason=None):
        coolpeople = discord.utils.get(ctx.author.roles, name="Cool People")
        if (str(
                ctx.message.channel) == "bot-commands" or coolpeople != None or ctx.message.author.guild_permissions.manage_messages):
            if reason == None:
                await ctx.send("Invalid syntax, please add the issue you are facing.")
            else:
                creator = await self.bot.fetch_user(554907015785218050)
                await creator.send(f"Reported by user {ctx.message.author} : " + reason)
                await ctx.send("Your report has been successfully forwarded to moderators")
        else:
            await ctx.send("Please use this command in `#bot-commands`")

    # reporting users
    @commands.command()
    async def report(self, ctx, user=None, *, reason=None):
        cool_people = discord.utils.get(ctx.author.roles, name="Cool People")
        if (str(
                ctx.message.channel) == "bot-commands" or cool_people is not None or
                ctx.message.author.guild_permissions.manage_messages):
            if reason is None or user is None:
                await ctx.send(f'Invalid syntax, please check `{self.bot.command_prefix}help` to check the syntax and '
                               f'pass proper arguments.')
            else:
                channel = discord.utils.get(ctx.message.author.guild.channels, name="moderators")
                await channel.send(f'Reported by user {ctx.message.author} : Complain against user {user} - ' + reason)
                await ctx.send('Your report has been successfully forwarded to moderators')
        else:
            await ctx.send('Please use this command in `#bot-commands`')

    # Suggestion command
    @commands.command()
    async def suggest(self, ctx, *, sug=None):
        cool_people = discord.utils.get(ctx.author.roles, name='Cool People')
        if (str(
                ctx.message.channel) == "bot-commands" or cool_people is not None
                or ctx.message.author.guild_permissions.manage_messages):
            if sug is None:
                await ctx.send("oops, seems like you forgot to add the suggestion .")
            else:
                channel = discord.utils.get(ctx.message.author.guild.channels, name="suggestions")
                emb = discord.Embed(description=sug, colour=0xff002a)
                emb.set_author(name=f'{ctx.message.author}', icon_url=f"{ctx.message.author.avatar_url}")
                emb.set_footer(text=f'Submit your suggestions using: '
                                    f'{self.bot.command_prefix}suggest <suggestion> in #bot-commands')
                msg = await channel.send(embed=emb)
                await msg.add_reaction('👍')
                await msg.add_reaction('👎')
                await ctx.send(f'Your suggestion has been added in {channel.mention}')
        else:
            await ctx.send('Please use this command in `#bot-commands`')


def setup(bot):
    bot.add_cog(GeneralCog(bot))
    print('General cog loaded')
