import discord 
from discord.ext import commands
import asyncio
import time
import random
import cogs.qna

class VerifyCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Current Verification method
    @commands.command(aliases=['verification'])
    async def verify(self, ctx):
        gotindex=[]
        i=0
        flag=0
        if(str(ctx.message.channel)=="welcome"):
            await ctx.message.author.send("**Hey Again, I hope you ready for verification quiz**\nVerification quiz will start in `30` secound hope you have read the rules properly, also you will have `60` seconds to answer each question so please read the question properly : )\n\nDon't worry, if verification fail please go back to welcome channel and again type `$verify` to re-verify yourself, or just ask moderators for help.")
            time.sleep(35)
            while True:
                index=random.randint(0,20)
                if index not in gotindex:
                    i+=1
                    gotindex.append(index)
                    question=cogs.qna.listofquestions[index]
                    answer=cogs.qna.answers[index]
                    await ctx.message.author.send("**Question : "+question+"[Answer as either `True` or `False`.]**")

                    def check(m):
                        return m.author == ctx.message.author 

                    try:
                        msg = await self.bot.wait_for('message', check=check, timeout = 60)
                        if msg.content.lower() == answer:
                            await ctx.message.author.send('Correct Answer\n')
                            time.sleep(1)
                        else:
                            await ctx.message.author.send('Wrong Answer.')
                            flag+=1
                            break
                    except asyncio.TimeoutError:
                        await ctx.message.author.send('Times out')
                    if i>=4:
                        break
                else:
                    continue
            if(flag>=1):
                await ctx.message.author.send(f"{ctx.message.author.mention} Verification failed, it seems you gave a wrong answer leading to this fail, please go through rules again and re-verify yourself(you can again use `$verify` command to verify yourself), if you have any other question or if you want to be manually verified, please wait for our veterans/moderators/admins, they will help you as soon as they see your texts in this channel. Note: Please don't ping a role, our team is already notified. :)")
                channel = discord.utils.get(ctx.message.author.guild.channels, name="verifications-help")
                await channel.send(f"Seems like {ctx.message.author}, failed his verification.. If anyone is online and free atm, please help that member, thank ya.. I will owe you one : P")
                await channel.send(f"log: {ctx.message.author} failed on this question: {question}")
                await channel.send("...")
            else:
                announ=0
                await ctx.message.author.send("**Question: Do you also want announcement role(it is for pings about server updates, polls, upcoming ctfs and such information.) ? [Answer as either `Yes` or `No`.]**")
                def check(m):
                    return m.author == ctx.message.author 
                try:
                    msg = await self.bot.wait_for('message', check=check, timeout = 60)
                    if msg.content.lower() == "yes":
                        announ+=1
                except asyncio.TimeoutError:
                    await ctx.message.author.send('Times out')
                role = discord.utils.get(ctx.guild.roles, name="Member")
                await ctx.message.author.add_roles(role)
                if(announ==1):
                    role = discord.utils.get(ctx.guild.roles, name="Announcements")
                    await ctx.message.author.add_roles(role)
                channel1 = discord.utils.get(ctx.message.author.guild.channels, name="bot-commands")
                channel2 = discord.utils.get(ctx.message.author.guild.channels, name="verifications-help")
                await ctx.message.author.send(f'**Welcome to the Server, **{ctx.message.author.mention} **!** \nWe are glad to have you here. if you wanna go through quick server description please go to {channel1.mention} and enter command `$chdesc` to get a description of almost every channel and `$faq` to get frequently asked questions.\nWe hope you enjoy your stay and contribute in our community : )')
                await channel2.send(f"log: {ctx.message.author} successfully verified")
        else:
            await ctx.send("Mate..You are already verified : )")

def setup(bot):
    bot.add_cog(VerifyCog(bot))
    print('Verification cog loaded')