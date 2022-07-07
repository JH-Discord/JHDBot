#!/usr/bin/env python3
import asyncio
import discord
import os
from discord.ext import commands


class VerifyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Current Verification method
    @commands.command(aliases=["verification"])
    async def verify(self, ctx, announcement_role=None):
        try:
            if str(ctx.message.channel) == os.getenv("WELCOME_CHANNEL"):
                role = discord.utils.get(ctx.guild.roles, name="Member")
                await ctx.message.author.add_roles(role)
                flag = 0
                if announcement_role == "announcement":
                    role = discord.utils.get(ctx.guild.roles, name="Announcements")
                    await ctx.message.author.add_roles(role)
                    flag += 1
                botchannel = discord.utils.get(ctx.message.author.guild.channels, name=os.getenv("BOT_COMMAND_CHANNEL"))
                try:
                    await ctx.message.author.send(
                        f'Welcome to the server {ctx.message.author.mention}!\n'
                        f'We are glad to have you here. If you wanna go through quick server description please go to {botchannel.mention} '
                        f'and enter command `$chdesc` to get a description of almost every channel and `$faq` to get frequently asked questions. '
                        f'We hope you enjoy your stay and contribute in our community : )\n'
                        )
                except Exception:
                    await ctx.send(f'Welcome to the server {ctx.message.author}! We are glad to have you here :D\n\n')
                channel = discord.utils.get(ctx.message.author.guild.channels, name='verifications-help')
                if(flag==1):
                    await channel.send(f'{ctx.message.author.mention} successfully verified. Roles given: `Member` and `Announcement`.')
                else:
                    await channel.send(
                        f"{ctx.message.author.mention} successfully verified. Roles given `Member`."
                    )
            else:
                await ctx.send("Command only works in #"+os.getenv("WELCOME_CHANNEL")+" channel : )")
            await asyncio.sleep(3)
            await ctx.message.delete()
        except Exception:
            await ctx.send(
                "Some error happened while executing the command, please reach out to moderators/admins."
            )


def setup(bot):
    bot.add_cog(VerifyCog(bot))
    print("Verification cog loaded")
