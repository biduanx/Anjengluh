import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "30"))

DEVS = list(map(int, os.getenv("DEVS", "7366711345").split()))

API_ID = int(os.getenv("API_ID", "21448110"))

API_HASH = os.getenv("API_HASH", "c2a04103f18bc9b30669b26a6fc88449")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7018391268:AAG-OaWPORQeajmaaQWfSjQCElOwh12Rkig")

OWNER_ID = int(os.getenv("OWNER_ID", "7366711345"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002864024582").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://kemem:kemem@cluster0.aqka4ti.mongodb.net/?appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1003055932888"))
