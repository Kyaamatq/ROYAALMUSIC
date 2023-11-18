from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "99999999"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/dc55b785e3e2c7b0026fa.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/cbce6e62048c493020ca4.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ll_friendss_chatting_group_ll")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ll_friendss_chatting_group_ll")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


ROYAAL = "https://graph.org/file/9256adef6b49b1ffeadf6.jpg"
