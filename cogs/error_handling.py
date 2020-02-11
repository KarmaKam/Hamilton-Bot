import discord
from discord.ext import commands
import datetime
from other.utils import *
import random
import bot
from cogs.owner_commands import *
from cogs.fun import *
from cogs.eightball import *
from cogs.misc import *
from cogs.urbandict import *


class Error_Handling(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            r = ['That is not a proper command..', 'I cannot perform a non-existent request.', 'Are you going to give me something to do, or what?', 'I cannot just sit here idly, what do you want me to do?']
            await ctx.send(f':x: {random.choice(r)}')
        elif isinstance(error, commands.CheckFailure):
            await ctx.send(f':x: You do not have the permissions to perform this command!')
        elif isinstance(error, commands.MissingRequiredArgument):
            if ctx.command.name.lower() == "say":
                r = ['What do you need me to say? It cannot be nothing.', 'Give me something to say.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.say [text]`']
                await ctx.send(f':x: {random.choice(r)}')
            if ctx.command.name.lower() == "say":
                r = ['What do you need me to say? It cannot be nothing.', 'Give me something to say.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.say [text]`']
                await ctx.send(f':x: {random.choice(r)}')
            if ctx.command.name.lower() == "status":
                r = ['Are you going to set a status or what?', 'A status cannot contain nothing, bonehead.',  'Try setting my status to something that is not nothing.', 'That is not a proper status, dolt.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.status [text]`']
                await ctx.send(f':x: {random.choice(r)}')
            if ctx.command.name.lower() == "define":
                r = ['I cannot search for something that does not exist...', 'Give me something to search for.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.define [word]`']
                await ctx.send(f':x: {random.choice(r)}')
            if ctx.command.name.lower() == "urban":
                r = ['I cannot search for something that does not exist...', 'Give me something to search for.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.define [word]`']
                await ctx.send(f':x: {random.choice(r)}')
            if ctx.command.name.lower() == "temperature":
                r = ['I cannot calculate a number that does not exist...', 'Give me something to calculate.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.temperature [number]`']
                await ctx.send(f':x: {random.choice(r)}')
            if ctx.command.name.lower() == "eightball":
                r = ['Are you going to ask me a question or what?', 'What is it that you want to ask? I am waiting...',  'Ask me a question, dimwit.', 'Will you ask me a question, or no? Make up your mind.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.8ball [yes/no question]`']
                await ctx.send(f':x: {random.choice(r)}')
            if ctx.command.name.lower() == "coinflip":
                r = [f'You need to specify an amount of wisps you\'re willing to bet, then choose heads {Emoji.heads} or tails {Emoji.tails}. The usage goes as follows; `ok.coinflip [amount] [heads/tails]`']
                await ctx.send(f':x: {random.choice(r)}')
        else:
            print(f'Something went wrong. Error: \n{error, type(error)}\nTime of error: {datetime.datetime.now()}')
            await ctx.send(f'Something went very wrong, let us laugh at Lerrific\'s incompetence... ```{error, type(error)}```')


def setup(client):
    client.add_cog(Error_Handling(client))
