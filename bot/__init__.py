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

USER_SESSION = os.environ.get("USER_SESSION", "BQF8ngYAxWYTOxdxa9Irv2R1vsduwIAzLM3rENhr-xvBY--0yPcfON2GgRjotpVSPGf_WEI5FeDecWpuV2fGlm0tTlolF6Q7qXecIgb0hOYr7V-4ujZmB_lcSUvAWCce9pySI-rV-o9YAoqpUT0ViSD-LTDbhy_gdRYqEO_VR3vBIJILAOX2R6YQH55iFtIXLxUro0BdSNyn8pABY9OO7pTUFOJZEdnrGUitOTSaWHW_6rYOcw2lM7Bb_OnB6DTe7_SeIRmKXLDR6qzgHapOaxHIzeBoEtNrp_9Zte0gwl5ARHP1PsDYIosCDmW3aXdW-0bDyXlHBjGV9lJTvFaXpslj2RMOfgAAAAGi62njAA")

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
