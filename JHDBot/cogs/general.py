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
        if await self.isAuthorized(ctx):
            await ctx.send(f'Ping! - {round(self.bot.latency * 1000)}ms')

    # For Likt
    @commands.command()
    async def solve(self, ctx, *, input=None):
        if await self.isAuthorized(ctx):
            await ctx.send("That is a definite maybe")

    # Report bot command
    @commands.command(aliases=['reportbot'])
    async def report_bot(self, ctx, *, reason=None):
        if await self.isAuthorized(ctx, veteran=False):
            if reason:
                dev_channel = await discord.utils.get(ctx.message.author.guild.channels, name="dev-team")
                await moderators_channel.send(f'Reported by user {ctx.message.author} : Complain against user {user} - {reason}')
                await ctx.send("Your report has been successfully forwarded to the devs")
            else:
                await ctx.send("Invalid syntax, please add the issue you are facing.")

    # reporting users
    @commands.command()
    async def report(self, ctx, user=None, *, reason=None):
        if await self.isAuthorized(ctx, veteran=False):
            if reason and user:
                moderators_channel = discord.utils.get(ctx.message.author.guild.channels, name="moderators")
                await moderators_channel.send(f'Reported by user {ctx.message.author} : Complain against user {user} - {reason}')
                await ctx.send('Your report has been successfully forwarded to moderators')
            else:
                await ctx.send(f'Invalid syntax, please check `{self.bot.command_prefix}help` to check the syntax and '
                               f'pass proper arguments.')
                

    # Suggestion command
    @commands.command()
    async def suggest(self, ctx, *, sug=None):
        if await self.isAuthorized(ctx, veteran=False):
            if sug:
                suggestions_channel = discord.utils.get(ctx.message.author.guild.channels, name="suggestions")
                emb = discord.Embed(description=sug, colour=0xff002a)
                emb.set_author(name=f'{ctx.message.author}', icon_url=f"{ctx.message.author.avatar_url}")
                emb.set_footer(text=f'Submit your suggestions using: '
                                    f'{self.bot.command_prefix}suggest <suggestion> in #bot-commands')
                msg = await suggestions_channel.send(embed=emb)
                await msg.add_reaction('👍')
                await msg.add_reaction('👎')
                await ctx.send(f'Your suggestion has been added in {suggestions_channel.mention}')
            else:
                await ctx.send("oops, seems like you forgot to add the suggestion .")
    
    async def isAuthorized(self, ctx, veteran=True, moderator=True):
        authorized_roles = []

        if veteran:     authorized_roles.append("Veteran")
        if moderator:   authorized_roles.append("Moderator Emeritus")

        user_roles = [discord.utils.get(ctx.author.roles, name=role) for role in authorized_roles]
        
        if (str(ctx.message.channel) == 'bot-commands' or user_roles[0] or user_roles[1]
            or ctx.message.author.guild_permissions.manage_messages):
            return True
        
        await ctx.send('Please use this command in `#bot-commands`')
        return False


def setup(bot):
    bot.add_cog(GeneralCog(bot))
    print('General cog loaded')