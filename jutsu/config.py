import os


class Config:
    LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID"))