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
    async def verify(self, ctx):
        if ctx.message.author.name == 'username123':
            await ctx.send('Please manually verify yourself')
        else:
            try:
                list_of_questions = [
                    'Can we help you get your Instagram account back?',
                    'Are we selling accounts?',
                    'Can we help you set up a botnet?',
                    'To get an answer to a question, should you ask it repeatedly in every channel?',
                    'You should totally dump all your flags here?',
                    'You should not link to graphic, illegal or NSFW content?',
                    'you should keep HTB nudges to Direct Messages?',
                    'You should report any broken rules or server member, with `$report [user mention] [reason]`.',
                    'Flag and hint sharing is not permitted on private CTFs?',
                    'Advertisement without permission is fine?',
                    'This is the right place to try out your new IP grabber or virus?',
                    'You can post illegal content here?',
                    'Is being nice is optional?',
                    'Is this is a blackhat server?',
                    'You should be nice to all server members?',
                    'You should ask permission before sending a DM?',
                    'Is this is a whitehat discord server?',
                    'This is not a dark marketplace',
                    'Harassment in any form is not permitted.',
                    'When asking for help on a challenge you should specify where it comes from?',
                    'You get five warnings before being banned.',
                    'We can help you recover your Facebook account.',
                    'We can help you get your Roblox account back.',
                    'We cannot help you crack applications.',
                    'Self Advertising includes posting Discord invite links.',
                    'Flag sharing is allowed.',
                    'Harassment includes deliberate intimidation and targeting individuals in a manner that makes '
                    'them feel uncomfortable, unwelcome, or afraid.',
                    'We can help you make an aimbot.',
                    'You should have full permission and or ownership before doing any hacking.',
                    'You should help make this community welcoming for everyone.',
                    'We can help you get unbanned from _______.',
                    'Does repeatedly asking or begging people to look at a problem get people to help you?'
                ]

                answers = ['false', 'false', 'false', 'false', 'false', 'true', 'true', 'true', 'true', 'false',
                           'false', 'false', 'false', 'false', 'true', 'true', 'true', 'true', 'true', 'true', 'false',
                           'false', 'true', 'true', 'true', 'false', 'true', 'false', 'true', 'true', 'false', 'false']
                got_index = []
                i = 0
                flag = 0
                if str(ctx.message.channel) == 'welcome':
                    await ctx.message.author.send(
                        '**Hey Again, I hope you ready for verification quiz**\nVerification quiz will start in `30` '
                        'second hope you have read the rules properly, also you will have `60` seconds to answer each '
                        'question so please read the question properly, till the quiz begin please be patient and '
                        'don\'t type anything(else sometimes bot gets mad.) : )\n\nDon\'t worry, if verification fail '
                        'please go back to welcome channel and again type `$verify` to re-verify yourself, '
                        'or just ask moderators for help.')
                    await asyncio.sleep(30)
                    while True:
                        index = random.randint(0, 31)
                        if index not in got_index :
                            i += 1
                            got_index .append(index)
                            question = list_of_questions[index]
                            answer = answers[index]
                            await ctx.message.author.send(
                                f'_Question_ : {question} \n *[Answer as either `True` or `False`.]*')

                            def check(m):
                                return m.author == ctx.message.author

                            try:
                                msg = await self.bot.wait_for('message', check=check, timeout=60)
                                if msg.content.lower() == answer:
                                    await ctx.message.author.send('Correct Answer\n')
                                    time.sleep(1)
                                else:
                                    await ctx.message.author.send('Wrong Answer.')
                                    flag += 1
                                    break
                            except asyncio.TimeoutError:
                                flag += 1
                                break
                            if i >= 4:
                                break
                        else:
                            continue
                    if flag >= 1:
                        await ctx.message.author.send(
                            f'{ctx.message.author.mention} Verification failed, it seems you gave a wrong answer or '
                            f'the time ran out leading to this fail, please go through rules again and re-verify '
                            f'yourself(you can again use `{self.bot.command_prefix}verify` command to verify '
                            f'yourself), if you have any other '
                            f'question or if you want to be manually verified, please wait for our '
                            f'veterans/moderators/admins, they will help you as soon as they see your texts in this '
                            f'channel. Note: Please don\'t ping a role, the team has already been notified.')
                        channel = discord.utils.get(ctx.message.author.guild.channels, name='verifications-help')
                        await channel.send(
                            f'Seems like {ctx.message.author}, failed their verification.. If anyone is online and '
                            f'free atm, please help that member, thank ya.. I owe you one')
                        await channel.send(f'log: {ctx.message.author} failed on this question: {question}\n...')
                    else:
                        announ = 0
                        await ctx.message.author.send(
                            '**Question: Do you also want announcement role(it is for pings about server updates, '
                            'polls, upcoming CTFs and such information.)? [Answer as either `Yes` or `No`.]**')

                        def check(m):
                            return m.author == ctx.message.author

                        try:
                            msg = await self.bot.wait_for('message', check=check, timeout=60)
                            if msg.content.lower() == 'yes':
                                announ += 1
                        except asyncio.TimeoutError:
                            await ctx.message.author.send('Times out')
                        role = discord.utils.get(ctx.guild.roles, name='Member')
                        await ctx.message.author.add_roles(role)
                        if announ == 1:
                            role = discord.utils.get(ctx.guild.roles, name='Announcements')
                            await ctx.message.author.add_roles(role)
                        channel1 = discord.utils.get(ctx.message.author.guild.channels, name='bot-commands')
                        channel2 = discord.utils.get(ctx.message.author.guild.channels, name='verifications-help')
                        await ctx.message.author.send(
                            f'**Welcome to the Server, **{ctx.message.author.mention} **!** \nWe are glad to have you '
                            f'here. if you wanna go through quick server description please go to {channel1.mention} '
                            f'and enter command `{self.bot.command_prefix}chdesc` to get a description of almost '
                            f'every channel and `$faq` to '
                            f'get frequently asked questions.\nWe hope you enjoy your stay and contribute in our '
                            f'community : )')
                        await channel2.send(f"log: {ctx.message.author} successfully verified\n...")
                else:
                    await ctx.send("Command only works in #welcome channel : )")
            except:
                await ctx.send(
                    f'Hey {ctx.message.author.mention}, are you sure you have message from server member `on`, in your '
                    f'privacy settings because I am unable to DM you.')


def setup(bot):
    bot.add_cog(VerifyCog(bot))
    print('Verification cog loaded')
