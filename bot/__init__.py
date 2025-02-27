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

USER_SESSION = os.environ.get("USER_SESSION", "BQFP5NMABueBVZEYg_KLjJ86Q54L0CaArlWCy75dnJDef6VW2TaPB_sYbX9k9yxLKdhGssO2kWLrWGAtdDaSRVr8IQNkYFLBXe8T_ipuRyfBFDTis5zG12uIbjJubbi2BKlf4M4h4khSDrtCNjNGHamj0Mie5pXMALz2_B11w34q_d_atApUj6d35dWAIHDRQDhVdRklGU6WEUc5CMuEQphA4yrPB1Y5rqHibAroLzlyWzHFQtuBCMzzJDcpfCebb73MzPhosrMNAnnYKJnO6-PCXNwliCqmGPqxFTafH5tP4Po3mFs32dF0tKNrvPZmRMKBuwaoZKmtB258pYOFb8cNnPoregAAAAHObFO5AA")

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
