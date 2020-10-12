import discord
from discord.ext import commands
import asyncio
import random


class ModeratorCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Clear Message Command..
    @commands.command(name  = 'clear',
                      help  = 'Deletes messages',
                      usage = '[number of messages to delete]')  # a function to clear messages, if bot has perms to do that...
    async def clear(self, ctx,
                    amount=2):  # amount=2 sets the default value to 2 basically command + the text above that
        try:
            if ctx.message.author.guild_permissions.manage_messages:
                if(amount<=20):
                    await ctx.channel.purge(limit=amount + 1)  # limit= number of messages going to be deleted !
                    msg = await ctx.channel.send(f'Deleted {amount} messages D:')
                else:
                    await ctx.channel.send('Sorry, max 20 messages can be deleted at a time')
            else:
                msg = await ctx.send('Sorry, it seems like you are not authorized to do it')
            await asyncio.sleep(5)
            await msg.delete()
        except:
            await ctx.send('The bot is unauthorized to delete messages D:')

    # Mute Command..
    @commands.command(name  = 'mute',
                      help  = 'Mutes a specified user for some time.',
                      usage = '[user mention or id] [time in seconds]')  # a function to mute members
    async def mute(self, ctx, user: discord.Member,
                   seconds=None):  # gets context user and time(in seconds), default being None
        try:
            if ctx.message.author.guild_permissions.kick_members:
                if seconds is None or int(seconds) < 0:
                    # if no time supplied, function exits
                    await ctx.send('Please also supply time in seconds (proper +ve int format plz).')
                    return
                else:
                    # check perms. if user has perms to manage message like if he mod he can't be muted by the bot.
                    if user.guild_permissions.manage_messages:
                        await ctx.send(f'Sorry, can\'t mute {user} because of perms : (')
                        return
                    # add mute role
                    role = discord.utils.get(ctx.guild.roles, name='Muted')
                    muted_role = discord.utils.get(ctx.guild.roles, name='Member')
                    await user.add_roles(role)
                    await user.remove_roles(muted_role)
                    await user.send(f'You were muted in JHDiscord for `{seconds}` seconds')
                    await ctx.send(f'{user} has been muted in JHD for `{seconds}` seconds')
                    muted = discord.utils.get(user.roles, name="Muted")
                    if muted is not None:
                        await asyncio.sleep(int(seconds))
                        await user.remove_roles(role)
                        await user.add_roles(muted_role)
                        await user.send(
                            'You were un-muted in JHDiscord, we hope you don\'t repeat the actions that lead the '
                            'mods/admin to mute you.')
                        await ctx.send(f'{user} has been unmuted in JHD')
            else:
                await ctx.send('Sorry, it seems like you are not authorized to do it')
        except:
            await ctx.send('Seems like the Bot is not authorized to run this command')

    # unmute command..
    @commands.command(name  = 'unmute',
                      help  = 'Unmutes a specified user.',
                      usage = '[user mention or id]')
    async def unmute(self, ctx, user: discord.Member):
        try:
            if ctx.message.author.guild_permissions.kick_members:
                muted = discord.utils.get(user.roles, name='Muted')
                if muted is not None:
                    role = discord.utils.get(ctx.guild.roles, name='Muted')
                    mrole = discord.utils.get(ctx.guild.roles, name='Member')
                    await user.remove_roles(role)
                    await user.add_roles(mrole)
                    await user.send(
                        "You were un-muted in JHDiscord, we hope you don't repeat the actions that lead the "
                        "mods/admin to mute you.")
                    await ctx.send(f'{user} has been unmuted in JHD')
                else:
                    await ctx.send(f'{user} is not muted ¯\_(ツ)_/¯ ')
            else:
                await ctx.send('Sorry, it seems like you are not authorized to do it')
            await asyncio.sleep(5)
            await ctx.message.delete()
        except:
            await ctx.send('Seems like the Bot is not authorized to run this command')

            # Kick Member Command..

    @commands.command(name = 'kick',
                      help = 'Kicks a specified user.',
                      usage = '[user mention or id] [reason]')  # a function to kick members
    async def kick(self, ctx, user: discord.Member, *, reason=None):  # gets context user and reason, default being None
        try:
            list_of_kick_gif = [
                'https://tenor.com/view/anime-kick-go-out-gif-14290462',
                'https://tenor.com/view/kick-knock-out-hurt-ouch-gif-4799973',
                'https://tenor.com/view/drop-kicked-watch-this-gif-12761359'
            ]
            if user.guild_permissions.manage_messages:
                # check perms. if user has perms to manage message like if he mod he can't be kicked by the bot.
                await ctx.send(f'Sorry, can\'t kick {user} because of their current permissions.')
            elif ctx.message.author.guild_permissions.kick_members:
                # checks if user who send the kick command is authorized to do it.
                await user.send(f'You were kicked from JHDiscord : {reason}')
                val = random.randint(0,2)
                await user.send(list_of_kick_gif[val])
                await ctx.guild.kick(user=user, reason=reason)  # kicks that user
                await ctx.send(f'{user} has been kicked out from the server')
                await ctx.send(list_of_kick_gif[val])
            else:
                await ctx.send('Sorry, it seems like you are not authorized to do it')
            await asyncio.sleep(5)
            await ctx.message.delete()
        except:
            await ctx.send('The bot is unauthorized to kick members.')

    # Ban Member Command..
    @commands.command(name  = 'ban',
                      help  = 'Bans a specified user.',
                      usage = '[user mention or id] [reason]')  # a function to ban members
    async def ban(self, ctx, user: discord.Member, *, reason=None):  # gets context user and reason, default being None
        try:
            list_of_ban_gif = [
                'https://tenor.com/view/blob-banned-ban-hammer-blob-ban-emoji-gif-16021044',
                'https://tenor.com/view/banned-thor-banned-thor-ban-thor-admin-gif-12850590',
                'https://tenor.com/view/salt-bae-ban-banned-gif-10497201'
            ]
            if user.guild_permissions.manage_messages:
                # check perms. if user has perms to manage message like if he mod he can't be banned by the bot.
                await ctx.send(f'Sorry, can\'t ban {user} because of perms : (')
            elif ctx.message.author.guild_permissions.ban_members:
                # checks if user who send the ban command is authorized to do it.
                await user.send(f'You were kicked from JHDiscord : {reason}')
                val = random.randint(0,2)
                await user.send(list_of_ban_gif[val])
                await ctx.guild.ban(user=user, reason=reason)  # bans that user
                await ctx.send(f'{user} has been banned from the server')
                await ctx.send(list_of_ban_gif[val])
            else:
                await ctx.send('Sorry, it seems like you are not authorized to do it')
            await asyncio.sleep(5)
            await ctx.message.delete()
        except:
            await ctx.sent('The bot is unauthorized to ban members.')

    # MultiKick Member Command..
    @commands.command(name = 'multikick', hidden = True)  # a function to multikick members
    async def multikick(self, ctx, *, users):  # gets user ids in string.
        try:
            if ctx.message.author.guild_permissions.kick_members:
                listofusers = users.split()
                reason = 'Kicked during a multikick process, Most probably we suspect you to be a bot if you are not please rejoin later.'
                for i in listofusers:
                    user = await self.bot.fetch_user(i[3:-1])
                    try:
                        await user.send(f'You were kicked from JHDiscord : {reason}')
                        await ctx.guild.kick(user=user, reason=reason)  # kicks that user
                        await ctx.send(f'{user} has been kicked out from the server')
                    except:
                        await ctx.send(f'Can\'t kick the user because of his permission, though he|she might have got a kick message.')
            else:
                await ctx.send('Sorry, it seems like you are not authorized to do it')
            await asyncio.sleep(5)
            await ctx.message.delete()
        except:
            await ctx.send('The bot is unauthorized to kick members.')


    # Multiban Member Command..
    @commands.command(name = 'multiban', hidden = True)  # a function to multiban members
    async def multiban(self, ctx, *, users):  # gets user id in string.
        try:
            if ctx.message.author.guild_permissions.kick_members:
                listofusers = users.split()
                reason = 'Banned during a multiban process, Most probably we are sure you to be a bot if you are not reach to our staff on other servers, like THM, HTB, yada yada.'
                for i in listofusers:
                    user = await self.bot.fetch_user(i[3:-1])
                    try:
                        await user.send(f'You were banned from JHDiscord : {reason}')
                        await ctx.guild.ban(user=user, reason=reason)  # bans that user
                        await ctx.send(f'{user} has been banned out from the server')
                    except:
                        await ctx.send(f'Can\'t ban the user because of his permission, though he|she might have got a ban message.')
            else:
                await ctx.send('Sorry, it seems like you are not authorized to do it')
            await asyncio.sleep(5)
            await ctx.message.delete()
        except:
            await ctx.send('The bot is unauthorized to ban members.')

def setup(bot):
    bot.add_cog(ModeratorCog(bot))
    print('Moderation cog loaded')
