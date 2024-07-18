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

USER_SESSION = os.environ.get("USER_SESSION", "BQG_NJ0ADVJqnP93SlXmepXCNlBl7Q9Ph8Mmx85HHO7TJAMvXwTyZcq7bNQWvdudHh13Qlx1K7wwcG-2JAjXkEiXrOrTKPgt8T1obrriA9lcmWW2FbGLPCmJWkuzYPYlB-11L5tq6jopJgoqfeBqJpCqWzGS2GzmwfOSl9P-Fd0uaJ3vKfLOvhqhO6W-lJmqlb7e0bE13mGn1Ke8hYH1H-Zk_NscFVIV5CjuJjIZk0CHdK3MmbrgxfV52sXldpqxlP_VwsrPfU1b4hc0Uw4UBigx8BiA4-fquUQWQ9CBpysvX2g48SyE9yzfYEr1sc4E4dMJLWnDjm-YIUnxYDYBS-B84r7wAAAAFVDeYoAA")

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
