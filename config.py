#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) TRTECHGUIDE

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "3393749"))
    API_HASH = os.environ.get("API_HASH", "a15a5954a1db54952eebd08ea6c68b71")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5409934939:AAGFr8CYJ1iUW_ZNBprJPH80RkrhkazEjfQ") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", None)
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", 12345)
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", 12345))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
