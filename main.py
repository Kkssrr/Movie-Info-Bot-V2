# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os
from pyrogram import Client

bot_token = os.environ["5517278922:AAGGG1NP__3FppgfJVzW96ZP4AOaS22VANk"]
api_id = int(os.environ["11604258"])
api_hash = os.environ["447e00413945ab1a61882f9e474477d6"]

plugins = dict(
    root="plugins"
)

Bot = Client(
    "Movie-Info-Bot-V2",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
    plugins=plugins
)

Bot.run()
