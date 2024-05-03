#-------------------------------------- https://github.com/m4mallu/PMChatbot ------------------------------------------#
import os

class Config(object):
    TG_BOT_TOKEN = int(os.environ.get("TG_BOT_TOKEN", "7115283463:AAEJhZjEIXcP06J4Z3iHh_x3X9FU6N6S-uw"))
    APP_ID = int(os.environ.get("APP_ID", 13223132))
    API_HASH = int(os.environ.get("API_HASH", "123120ee6712a97e0e413425b32cee48"))
    ADMIN = int(os.environ.get("ADMIN", 6694682223))
