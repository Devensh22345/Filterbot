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

USER_SESSION = os.environ.get("USER_SESSION", "BQG_NJ0AFQW4cs0lQEEIuzKatDskKLN7u18X7PS-SZ5Z-iMYIVDR2B3gVqt9y8LaojaCLogGHeBURS2ddoCDH9vZ7-86352iFMBmfKhvn-vvB2NVxtQ9Pl7pDsfRneZ5ZPhCeEX9WRNdsSnIp10T3mMt9EigCYEuzs7iPsRk5p8ORjG2YDFhB717gAvX2ZbpbAEKHDvGy6ldwkezx5CtiVyK-g9e4Pq6bJnWs3HwGtZoYxxxMEehyoPrhU_CBSle9z9QtYZAaHsGSMWfwv-iM29D6LQ07648OFDaoAlDtFn0OZ0thRO7kml8jyI4OstImUwXfeqTZyU1TglUBVjOOu-rmiIL9wAAAAFVDeYoAA")

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
