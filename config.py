# -*- coding: utf-8 -*-
import os

from werobot.config import Config

env_dist = os.environ

config = Config(
    SERVER="auto",
    HOST="127.0.0.1",
    PORT="8888",
    SESSION_STORAGE=None,
    APP_ID=env_dist.get('APP_ID'),
    APP_SECRET=env_dist.get('APP_SECRET'),
    TOKEN=env_dist.get('TOKEN'),
    ENCODING_AES_KEY=env_dist.get('ENCODING_AES_KEY')
)
