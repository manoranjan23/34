from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = getenv("API_ID","28228075")
API_HASH = getenv("API_HASH","785f20222ea7de471d714c1d563c59df")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))

OWNER_ID = getenv("OWNER_ID","7070591202")

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/b3d0e737737d67a5bf5a5.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sastatony")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/team_ligit")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
