import firebase_admin
from .guild import Guild
from .guild_setting import Setting
from .guild_dict import GuildDict
from .user_setting import UserSetting
from firebase_admin import credentials
from firebase_admin import firestore
import os
import concurrent.futures


class FireStore:
    def __init__(self, bot):
        """
        プランと残り文字数、プランへお金を出した人を保存する
        :param bot: discord.ext.commands.Bot
        """
        cred = credentials.Certificate(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))

        # TODO: credentialsをasyncio対応にする
        firebase_admin.initialize_app(cred)
        self.bot = bot
        self.db = firestore.client()
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=100)
        self.guild = Guild(self)
        self.setting = Setting(self)
        self.dict = GuildDict(self)
        self.user = UserSetting(self)
