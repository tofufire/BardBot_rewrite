import discord
from discord.ext import commands
from os import environ
from os.path import join, dirname
from dotenv import load_dotenv
from lib.firestore.firestore import FireStore
import asyncio
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def _prefix_callable(bot, msg):
    user_id = bot.user.id
    base = [f'<@!{user_id}> ',
            f'<@{user_id}> ',
            environ.get('prefix', '::'),
            'bard::',
            ]

    return base


class BardBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=_prefix_callable, help_command=None,
                         loop=asyncio.get_event_loop())

        self.firestore = FireStore(self)

    async def on_ready(self):
        await self.change_presence(
            activity=discord.Game(
                name=f"{environ.get('prefix', '::')}help | 読み上げBot"
            )
        )
