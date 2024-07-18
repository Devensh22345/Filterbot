#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("APP_ID", "22207976"))

API_HASH = os.environ.get("API_HASH", "5c0ad7c48a86afac87630ba28b42560d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6950804379:AAEos419_ptoLN0IimtWRQcLy-2MzTnpU7U")

DB_URI = os.environ.get("DB_URI", "mongodb+srv://Autofilterbot:Autofilterbot@cluster0.1oipdqu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

USER_SESSION = os.environ.get("USER_SESSION", "BQBy5STBOLqrAQY4e_NY267m7nwFiuS_7kH8UqGBqsNR1PGr4GqmoTfrfjYxVhPaIiuJFSv1cSsZKGQlR4SJX2zCcMPRyvTXmh-EOS4slOmze9ykrclMwRRE14LrDWvv-uPTM07HZ9fAd0BSc7_yZ2hopatydv5sgAHeamavO6Z_Gdfv_gQoKu7ZP6rqt5-qN4ugnaQ47uJ4bhc1ht-rxZy0iQN9vtD8FMvnQBHpiX-gHh_SEXpqkLch9F5NtiwVJ6PzW09AQnBfDfvNS2V-F3x2qbohwSD4Pfb5XFneLr8b69xUKR3TgeZmuuCZiMtlaFSZJa059uYERcuwCX1uXWAAAAAVUN5igA")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
