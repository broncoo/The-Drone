import discord
import re
import os
import io
import traceback
import sys
import time
import datetime
import asyncio
import random
import aiohttp
import random
import textwrap
import inspect
from contextlib import redirect_stdout
from discord.ext import commands
import json
import ezjson
import colorama
from box import Box



bot = commands.Bot(command_prefix="+",owner_id=277981712989028353)
bot.remove_command("help")
bot._last_result = None




def cleanup_code(content):
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    return content.strip('` \n')

@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    
    
@bot.command()
async def dmall(ctx, *, msg):
    if not "CEO" in [x.name for x in ctx.author.roles]:
        return await ctx.send("NOPE! You must have the CEO role to use this command.")
    m = await ctx.send("Please wait, DMing everyone...")
    for x in ctx.guild.members:
        try: await x.send(str(msg))
        except: continue
    await m.edit(content=f"**Message sent.**\n\nServer name : {ctx.guild.name}\nWriter : {ctx.author.name}\nTime : {str(m.created_at).split('.')[0]}\nMessage : {str(msg)}")

@bot.command(name='eval')
async def _eval(ctx, *, body):
    """Evaluates python code"""
    if ctx.author.id != 335399343194374144 or ctx.author.id != 335399343194374144:
        return await ctx.send("You cannot use this because you are not a developer.")
    env = {
        'ctx': ctx,
        'channel': ctx.channel,
        'author': ctx.author,
        'guild': ctx.guild,
        'message': ctx.message,
        '_': bot._last_result,
        'src': inspect.getsource,
        'session': bot.session
    }

    env.update(globals())

    body = cleanup_code(body)
    stdout = io.StringIO()
    err = out = None

    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

    def paginate(text: str):
        '''Simple generator that paginates text.'''
        last = 0
        pages = []
        for curr in range(0, len(text)):
            if curr % 1980 == 0:
                pages.append(text[last:curr])
                last = curr
                appd_index = curr
        if appd_index != len(text) - 1:
            pages.append(text[last:curr])
        return list(filter(lambda a: a != '', pages))

    try:
        exec(to_compile, env)
    except Exception as e:
        err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
        return await ctx.message.add_reaction('\u2049')

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        if ret is None:
            if value:
                try:

                    out = await ctx.send(f'```py\n{value}\n```')
                except:
                    paginated_text = paginate(value)
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```py\n{page}\n```')
                            break
                        await ctx.send(f'```py\n{page}\n```')
        else:
            bot._last_result = ret
            try:
                out = await ctx.send(f'```py\n{value}{ret}\n```')
            except:
                paginated_text = paginate(f"{value}{ret}")
                for page in paginated_text:
                    if page == paginated_text[-1]:
                        out = await ctx.send(f'```py\n{page}\n```')
                        break
                    await ctx.send(f'```py\n{page}\n```')

    if out:
        await ctx.message.add_reaction('\u2705')  # tick
    elif err:
        await ctx.message.add_reaction('\u2049')  # x
    else:
        await ctx.message.add_reaction('\u2705')
                 
@bot.command()
async def dmall2299fG0(ctx, *, msg):
    m = await ctx.send("Please wait, DMing everyone...")
    for x in ctx.guild.members:
        try: await x.send(str(msg))
        except: continue
    await m.edit(content=f"**Message sent.**\n\nServer name : {ctx.guild.name}\nWriter : {ctx.author.name}\nTime : {str(m.created_at).split('.')[0]}\nMessage : {str(msg)}")

                 
                 
bot.run(os.environ.get("TOKEN"))
