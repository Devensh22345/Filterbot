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

USER_SESSION = os.environ.get("USER_SESSION", "BQF8ngYAjhmhI-nGWDc6iSiPmg1dkW1gyYv6c_RPClJGhcqy1rO7z8OTnalffD43j5c0fHxk0wlLm5UCfYkdpHL9uNKJWNHI5RT0SJVy7AHUa_H1r9wgWtx4ENDWJGDpy7bSu0bu4Gln-H5ywYSMlc9Cj8m_euHH02Aw3t2ZnNWD1mYUBpUMDBuK-bhRo4dEqQE-KjnwV7hxscteQuiQb_aukb5RJ853OkXIKoUOZv7HKRwGNO4g6ANkaz35o1Le4Bu3_cAqgBl4pjb2QUvghiw4DEcwBr5Gu7WyWeOIptXVLNtgPJSdgDb9pVKzzp1SAYSGoc4tiGhfx506dtwqdjF1nt9qtwAAAAGi62njAA")

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
