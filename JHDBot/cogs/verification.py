import discord
from discord.ext import commands
import asyncio
import time
import random


class VerifyCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Current Verification method
    @commands.command(aliases=['verification'])
    async def verify(self, ctx, announcement_role=None):
        #try:
            if str(ctx.message.channel) == 'welcome':
                role = discord.utils.get(ctx.guild.roles, name='Member')
                await ctx.message.author.add_roles(role)
                flag=0
                if(announcement_role.lower()=="announcement"):
                    role = discord.utils.get(ctx.guild.roles, name='Announcements')
                    await ctx.message.author.add_roles(role)
                    flag+=1
                await ctx.send(f'Welcome to the server {ctx.message.author}, We are glad to have you here :D\n\n')
                channel = discord.utils.get(ctx.message.author.guild.channels, name='verifications-help')
                if(flag==1):
                    await channel.send(f'{ctx.message.author.mention} successfuly verified, Roles given `Member` and `Announcement`.')
                elif(flag==0):
                    await channel.send(f'{ctx.message.author.mention} successfuly verified, Roles given `Member`.')
                else:
                    await channel.send(f'Some Error happened while executing the command, please reach out to moderators/admins.')
            else:
                await ctx.send("Command only works in #welcome channel : )")
        #except:
        #    await ctx.send(f'Some Error happened while executing the command, please reach out to moderators/admins.')


def setup(bot):
    bot.add_cog(VerifyCog(bot))
    print('Verification cog loaded')
