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

USER_SESSION = os.environ.get("USER_SESSION", "BAFINEQAL797B4mtcyOvRUkhOh3JjYDzWyPrjUGngNiQca8ccKCBZ4zirQPc7456WrtzjQI_thMcykoDDZaQiuNFEI-dW_RJTI-UJfkvCwo8w1KbUEVj658W3CBUSEP_LAR7xMnomKWUjgj3t71la7y-CaLVXsM2qGpOWTqO9fsXNq03fRe561wLujdfeKr2xEXlDUeKlIcBJA-fRlPNoiWQ5IksQvJSFbVZRP1mFqi7ij9HVElYQ9tHAg9wqq99xoJuhPPEo28X09GAXPkXUI3mxmhbAsfq2-suwKbp5kRxQ_4ehev97WYeVdOe401W-4kKsoZ8CU71nyuPYjzH5ABe0feSMgAAAAGmVgSYAA")

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
