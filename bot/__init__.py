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

USER_SESSION = os.environ.get("USER_SESSION", "BQG_NJ0ATzJbjtXym2IffEdPVAUL_0ACokIQiVlKq6UEQlsNDt7P7_vIrALgE83A0DAc9t-WFo1kL1elnybQgAX1l0fR_-KEOTw6E3MMlge9__JS0oo-ijnmgQQNrJnXplXQqlmXC2L9Aod_SffYBy156NQtwTvj88t0SQTMM4kHtgH2hih-If1B7ajnfPq8EoPLYZQhjZIf_7x2bDcyn_lZVMozjhEzqYIWZaU_70KzjqRWqXTPjBBukR1v0I5RJQWsRbZo6H58EA1kQWo_JuvZMLsSyrfFKq0GWEzf8rIwXbJ2D90QpoM1N_ihriL-NeANYR5qNOxngb6w9eHOqXwm0nNqZwAAAAFVDeYoAA")

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
