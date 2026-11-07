import os
import json
import datetime
import sqlite3
from http.server import BaseHTTPRequestHandler
import telebot
from telebot import types

# ==========================================
# 🚀 M.K HACKER OFFICIAL CONFIG & SYSTEM CORE
# ==========================================
TOKEN = os.environ.get("BOT_TOKEN", "8891413386:AAEDJkXrzf7_BA_urUlNtvyhHAIJRU6TZnU")
bot = telebot.TeleBot(TOKEN, threaded=False)

CHANNEL_ID = "-1004404606781"            # Force Subscribe Channel ID
LOG_CHANNEL_ID = -1004320753506         # Data Log Channel ID
BROADCAST_CHANNEL_ID = -1004322168174   # Broadcast Channel ID

CHANNEL_INVITE_LINK = "https://t.me/MK_HACKERR586"
OWNER_CONTACT = "https://t.me/MK_HACKERR586"
BRAND_NAME = "😈☠️ 𝗠.𝗞 𝗛𝗔𝗖𝗞𝗘𝗥 ☠️😈"
BOT_NAME = "😈😘么𝐌.𝐊 𝐇𝐀𝐂𝐊𝗘𝐑 𝐅𝐎𝐍𝐓'𝐒 𝐁𝐎𝐓么😘😈"
BOT_USERNAME = "@MK_HACKER_FONTS_BOT"

DB_FILE = "/tmp/hacker_bot_pro_max.db"

# ==========================================
# 🗄️ SQLITE DATABASE & PERMANENT STORAGE
# ==========================================
def init_enterprise_db():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                full_name TEXT,
                joined_date TEXT,
                vip_status TEXT DEFAULT 'ELITE',
                conversions_count INTEGER DEFAULT 0
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS saved_fonts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                font_name TEXT,
                sample_text TEXT,
                saved_date TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS activity_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                action_type TEXT,
                payload TEXT,
                timestamp TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS counters (
                key TEXT PRIMARY KEY,
                value INTEGER
            )
        ''')
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"DB Init Error: {e}")

init_enterprise_db()

def get_next_request_count():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM counters WHERE key='request_count'")
        row = cursor.fetchone()
        count = (row[0] + 1) if row else 1
        cursor.execute("INSERT OR REPLACE INTO counters (key, value) VALUES ('request_count', ?)", (count,))
        conn.commit()
        conn.close()
        return count
    except Exception as e:
        return 1

def save_user_enterprise(user_id, username, full_name):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        pkt_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=5)).strftime("%d %b %Y, %I:%M %p")
        cursor.execute('''
            INSERT OR IGNORE INTO users (user_id, username, full_name, joined_date, conversions_count)
            VALUES (?, ?, ?, ?, 0)
        ''', (user_id, username, full_name, pkt_time))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"User save error: {e}")

def log_activity_enterprise(user_id, action, payload):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        pkt_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=5)).strftime("%d %b %Y, %I:%M %p")
        cursor.execute('''
            INSERT INTO activity_history (user_id, action_type, payload, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (user_id, action, payload, pkt_time))
        cursor.execute("UPDATE users SET conversions_count = conversions_count + 1 WHERE user_id = ?", (user_id,))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Activity log error: {e}")

def get_user_profile_data(user_id):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT joined_date, vip_status, conversions_count FROM users WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()
        return row if row else ("07 Nov 2026, 04:36 PM", "ELITE", 0)
    except Exception as e:
        return ("07 Nov 2026, 04:36 PM", "ELITE", 0)

def save_font_bookmark(user_id, name, text):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        pkt_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=5)).strftime("%d %b %Y")
        cursor.execute('''
            INSERT INTO saved_fonts (user_id, font_name, sample_text, saved_date)
            VALUES (?, ?, ?, ?)
        ''', (user_id, name, text, pkt_time))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Bookmark error: {e}")

def get_user_bookmarks(user_id):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT font_name, sample_text, saved_date FROM saved_fonts WHERE user_id = ? ORDER BY id DESC LIMIT 15", (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        return []

def get_all_registered_users():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users")
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]
    except Exception as e:
        return []

# ==========================================
# 🎨 COMPLETE 30+ PRO SERIF & STYLISH FONTS
# ==========================================
FONTS = {
    "f1": {"name": "𝐁𝐨𝐥𝐝 𝐒𝐞𝐫𝐢𝐟", "map": {"A": "𝐀", "B": "𝐁", "C": "𝐂", "D": "𝐃", "E": "𝐄", "F": "𝐅", "G": "𝐆", "H": "𝐇", "I": "𝐈", "J": "𝐉", "K": "𝐊", "L": "𝐋", "M": "𝐌", "N": "𝐍", "O": "𝐎", "P": "𝐏", "Q": "𝐐", "R": "𝐑", "S": "𝐒", "T": "𝐓", "U": "𝐔", "V": "𝐕", "W": "𝐖", "X": "𝐗", "Y": "𝐘", "Z": "𝐙", "a": "𝐚", "b": "𝐛", "c": "𝐜", "d": "𝐝", "e": "𝐞", "f": "𝐟", "g": "𝐠", "h": "𝐡", "i": "𝐢", "j": "𝐣", "k": "𝐤", "l": "𝐥", "m": "𝐦", "n": "𝐧", "o": "𝐨", "p": "𝐩", "q": "𝐪", "r": "𝐫", "s": "𝐬", "t": "𝐭", "u": "𝐮", "v": "𝐯", "w": "𝐰", "x": "𝐱", "y": "𝐲", "z": "𝐳", "0": "𝟎", "1": "𝟏", "2": "𝟐", "3": "𝟑", "4": "𝟒", "5": "𝟓", "6": "𝟔", "7": "𝟕", "8": "𝟖", "9": "𝟗"}},
    "f2": {"name": "𝐼𝑡𝑎𝑙𝑖𝑐 𝑆𝑒𝑟𝑖𝑓", "map": {"A": "𝐴", "B": "𝐵", "C": "𝐶", "D": "𝐷", "E": "𝐸", "F": "𝐹", "G": "𝐺", "H": "𝐻", "I": "𝐼", "J": "𝐽", "K": "𝐾", "L": "𝐿", "M": "𝑀", "N": "𝑁", "O": "𝑂", "P": "𝑃", "Q": "𝑄", "R": "𝑅", "S": "𝑆", "T": "𝑇", "U": "𝑈", "V": "𝑉", "W": "𝑊", "X": "𝑋", "Y": "𝑌", "Z": "𝑍", "a": "𝑎", "b": "𝑏", "c": "𝑐", "d": "𝑑", "e": "𝑒", "f": "𝑓", "g": "𝑔", "h": "ℎ", "i": "𝑖", "j": "𝑗", "k": "𝑘", "l": "𝑙", "m": "𝑚", "n": "𝑛", "o": "𝑜", "p": "𝑝", "q": "𝑞", "r": "𝑟", "s": "𝑠", "t": "𝑡", "u": "𝑢", "v": "𝑣", "w": "𝑤", "x": "𝑥", "y": "𝑦", "z": "𝑧", "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}},
    "f3": {"name": "𝘽𝙤𝙡𝙙 𝙄𝙩𝙖𝙡𝙞𝙘 𝙎𝙚𝙧𝙞𝙛", "map": {"A": "𝘼", "B": "𝘽", "C": "𝘾", "D": "𝘿", "E": "𝙀", "F": "𝙁", "G": "𝙂", "H": "𝙃", "I": "𝙄", "J": "𝙅", "K": "𝙆", "L": "𝙇", "M": "𝙈", "N": "𝙉", "O": "𝙊", "P": "𝙋", "Q": "𝙌", "R": "𝙍", "S": "𝙎", "T": "𝙏", "U": "𝙐", "V": "𝙑", "W": "𝙒", "X": "𝙓", "Y": "𝙔", "Z": "𝙕", "a": "𝙖", "b": "𝙗", "c": "𝙘", "d": "𝙙", "e": "𝙚", "f": "𝙛", "g": "𝙜", "h": "𝙝", "i": "𝙞", "j": "𝙟", "k": "𝙠", "l": "𝙡", "m": "𝙢", "n": "𝙣", "o": "𝙤", "p": "𝙥", "q": "𝙦", "r": "𝙧", "s": "𝙨", "t": "𝙩", "u": "𝙪", "v": "𝙫", "w": "𝙬", "x": "𝙭", "y": "𝙮", "z": "𝙯", "0": "𝟬", "1": "𝟭", "2": "𝟮", "3": "𝟯", "4": "𝟰", "5": "𝟱", "6": "𝟲", "7": "𝟳", "8": "𝟴", "9": "𝟵"}},
    "f4": {"name": "𝔊𝔬𝔱𝔥𝔦𝔠 𝔖𝔢𝔯𝔦𝔣", "map": {"A": "𝔄", "B": "𝔅", "C": "ℭ", "D": "𝔇", "E": "𝔈", "F": "𝔉", "G": "𝔊", "H": "ℌ", "I": "ℑ", "J": "𝔍", "K": "𝔎", "L": "𝔏", "M": "𝔐", "N": "𝔑", "O": "𝔒", "P": "𝔓", "Q": "𝔔", "R": "ℜ", "S": "𝔖", "T": "𝔗", "U": "𝔘", "V": "𝔙", "W": "𝔚", "X": "𝔛", "Y": "𝔜", "Z": "ℨ", "a": "𝔞", "b": "𝔟", "c": "𝔠", "d": "𝔡", "e": "𝔢", "f": "𝔣", "g": "𝔤", "h": "𝔥", "i": "𝔦", "j": "𝔧", "k": "𝔨", "l": "𝔩", "m": "𝔪", "n": "𝔫", "o": "𝔬", "p": "𝔭", "q": "𝔮", "r": "𝔯", "s": "𝔰", "t": "𝔱", "u": "𝔲", "v": "𝔳", "w": "𝔴", "x": "𝔵", "y": "𝔶", "z": "𝔷", "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}},
    "f5": {"name": "𝕭𝖔𝖑𝖉 𝕲𝖔𝖙𝔥𝔦ꓮ", "map": {"A": "𝕬", "B": "𝕭", "C": "𝕮", "D": "𝕯", "E": "𝕰", "F": "𝕱", "G": "𝕲", "H": "𝕳", "I": "𝕴", "J": "𝕵", "K": "𝕶", "L": "𝕷", "M": "𝕸", "N": "𝕹", "O": "𝕺", "P": "𝕻", "Q": "𝕼", "R": "𝕽", "S": "𝕾", "T": "𝕿", "U": "𝖀", "V": "𝖁", "W": "𝖂", "X": "𝖃", "Y": "𝖄", "Z": "𝖅", "a": "𝖆", "b": "𝖇", "c": "𝖈", "d": "𝖉", "e": "𝖊", "f": "𝖋", "g": "𝖌", "h": "𝖍", "i": "𝖎", "j": "𝖏", "k": "𝖐", "l": "𝖑", "m": "𝖒", "n": "𝖓", "o": "𝖔", "p": "𝖕", "q": "𝖖", "r": "𝖗", "s": "𝖘", "t": "𝖙", "u": "𝖚", "v": "𝖛", "w": "𝖜", "x": "𝖝", "y": "𝖞", "z": "𝖟", "0": "𝟎", "1": "𝟏", "2": "𝟐", "3": "𝟑", "4": "𝟒", "5": "𝟓", "6": "𝟔", "7": "𝟕", "8": "𝟖", "9": "𝟗"}},
    "f6": {"name": "𝒞𝓊𝓇𝓈𝒾𝓋ℯ 𝒮ℯ𝓇𝒾𝒻", "map": {"A": "𝒜", "B": "ℬ", "C": "𝒞", "D": "𝒟", "E": "ℰ", "F": "ℱ", "G": "𝒢", "H": "ℋ", "I": "ℐ", "J": "𝒥", "K": "𝒦", "L": "ℒ", "M": "ℳ", "N": "𝒩", "O": "𝒪", "P": "𝒫", "Q": "𝒬", "R": "ℛ", "S": "𝒮", "T": "𝒯", "U": "𝒰", "V": "𝒱", "W": "𝒲", "X": "𝒳", "Y": "𝒴", "Z": "𝒵", "a": "𝒶", "b": "𝒷", "c": "𝒸", "d": "𝒹", "e": "ℯ", "f": "𝒻", "g": "ℊ", "h": "𝒽", "i": "𝒾", "j": "𝒿", "k": "𝓀", "l": "𝓁", "m": "𝓂", "n": "𝓃", "o": "ℴ", "p": "𝓅", "q": "𝓆", "r": "𝓇", "s": "𝓈", "t": "𝓉", "u": "𝓊", "v": "𝓋", "w": "𝓌", "x": "𝓍", "y": "𝓎", "z": "𝓏", "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}},
    "f7": {"name": "𝓑𝓸𝓵𝓭 𝒞𝓊𝓇𝓈𝒾𝓋ℯ", "map": {"A": "𝓐", "B": "𝓑", "C": "𝓒", "D": "𝓓", "E": "𝓔", "F": "𝓕", "G": "𝓖", "H": "ℋ", "I": "𝓘", "J": "𝓙", "K": "𝓚", "L": "𝓛", "M": "𝓜", "N": "𝓝", "O": "𝓞", "P": "𝓟", "Q": "𝓠", "R": "ℛ", "S": "𝓢", "T": "𝓣", "U": "𝓤", "V": "𝓥", "W": "𝓦", "X": "𝓧", "Y": "𝓨", "Z": "𝓩", "a": "𝓪", "b": "𝓫", "c": "𝓬", "d": "𝓭", "e": "𝓮", "f": "𝓯", "g": "𝓰", "h": "𝓱", "i": "𝓲", "j": "𝓳", "k": "𝓴", "l": "𝓵", "m": "𝓶", "n": "𝓷", "o": "𝓸", "p": "𝓹", "q": "𝓺", "r": "𝓻", "s": "𝓼", "t": "𝓽", "u": "𝓾", "v": "𝓿", "w": "𝔀", "x": "𝔁", "y": "𝔂", "z": "𝔃", "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}},
    "f8": {"name": "𝕯𝖔𝖚𝖇𝖑𝖊 𝕾𝖙𝖗𝖚𝖈𝖐", "map": {"A": "𝔸", "B": "𝔹", "C": "ℂ", "D": "𝔻", "E": "𝔼", "F": "𝔽", "G": "𝔾", "H": "ℍ", "I": "𝕀", "J": "𝕁", "K": "𝕂", "L": "𝕃", "M": "𝕄", "N": "ℕ", "O": "𝕆", "P": "ℙ", "Q": "ℚ", "R": "ℝ", "S": "𝕊", "T": "𝕋", "U": "𝕌", "V": "𝕍", "W": "𝕎", "X": "𝕏", "Y": "𝕐", "Z": "ℤ", "a": "𝕒", "b": "𝕓", "c": "𝕔", "d": "𝕕", "e": "𝕖", "f": "𝕗", "g": "𝕘", "h": "𝕙", "i": "𝕚", "j": "𝕛", "k": "𝕜", "l": "𝕝", "m": "𝕞", "n": "𝕟", "o": "𝕠", "p": "𝕡", "q": "𝕢", "r": "𝕣", "s": "𝕤", "t": "𝕥", "u": "𝕦", "v": "𝕧", "w": "𝕨", "x": "𝕩", "y": "𝕪", "z": "𝕫", "0": "𝟘", "1": "𝟙", "2": "𝟚", "3": "𝟛", "4": "𝟜", "5": "𝟝", "6": "𝟞", "7": "𝟟", "8": "𝟠", "9": "𝟡"}},
    "f9": {"name": "𝚷𝓇ℴ 𝒮ℯ𝓇𝒾𝒻 ℬℴ𝓁𝒹", "map": {"A": "𝚷", "B": "𝐁", "C": "𝐂", "D": "𝐃", "E": "𝐄", "F": "𝐅", "G": "𝐆", "H": "𝐇", "I": "𝚰", "J": "𝐉", "K": "𝐊", "L": "𝐋", "M": "𝐌", "N": "𝐍", "O": "𝐎", "P": "𝐏", "Q": "𝐐", "R": "𝐑", "S": "𝕾", "T": "𝐓", "U": "𝐔", "V": "𝐕", "W": "𝐖", "X": "𝐗", "Y": "𝐘", "Z": "𝐙", "a": "𝐚", "b": "𝐛", "c": "𝐜", "d": "𝐝", "e": "𝐞", "f": "𝐟", "g": "𝐠", "h": "𝐡", "i": "𝐢", "j": "𝐣", "k": "𝐤", "l": "𝐥", "m": "𝐦", "n": "𝐧", "o": "𝐨", "p": "𝐩", "q": "𝕢", "r": "𝐫", "s": "𝐬", "t": "𝐭", "u": "𝐮", "v": "𝐯", "w": "𝐰", "x": "𝐱", "y": "𝐲", "z": "𝐳", "0": "𝟎", "1": "𝟏", "2": "𝟐", "3": "𝟑", "4": "𝟒", "5": "𝟓", "6": "𝟔", "7": "𝟕", "8": "𝟖", "9": "𝟗"}},
    "f10": {"name": "𝑅𝑜𝑦𝑎𝑙 𝒮ℯ𝓇𝒾𝒻", "map": {"A": "ℬ", "B": "ℬ", "C": "𝒞", "D": "𝒟", "E": "ℰ", "F": "ℱ", "G": "𝒢", "H": "ℋ", "I": "ℐ", "J": "𝒥", "K": "𝒦", "L": "ℒ", "M": "ℳ", "N": "𝒩", "O": "𝒪", "P": "𝒫", "Q": "𝒬", "R": "ℛ", "S": "𝒮", "T": "𝒯", "U": "𝒰", "V": "𝒱", "W": "𝒲", "X": "𝒳", "Y": "𝒴", "Z": "𝒵", "a": "𝒶", "b": "𝒷", "c": "𝒸", "d": "𝒹", "e": "ℯ", "f": "𝒻", "g": "𝑔", "h": "𝒽", "i": "𝒾", "j": "𝒿", "k": "𝓀", "l": "𝓁", "m": "𝓂", "n": "𝓃", "o": "ℴ", "p": "𝓅", "q": "𝓆", "r": "𝓇", "s": "𝓈", "t": "𝓉", "u": "𝓊", "v": "𝓋", "w": "𝓌", "x": "𝓍", "y": "𝓎", "z": "𝓏", "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}}
}

def apply_font(text, font_key):
    font_data = FONTS.get(font_key)
    if not font_data:
        return text
    return "".join(font_data["map"].get(char, char) for char in text)

user_state = {}

def verify_user_membership(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        if member.status in ["member", "creator", "administrator", "restricted"]:
            return True
    except Exception as e:
        print(f"Subscription check error: {e}")
    return False

# ==========================================
# 📊 DATA LOG CHANNEL FUNCTION
# ==========================================
def send_data_to_log_channel(message, source_action):
    try:
        user = message.from_user
        if not user:
            return

        user_id = user.id
        username = f"@{user.username}" if user.username else "𝐍𝐨 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞"
        full_name = f"{user.first_name or ''} {user.last_name or ''}".strip()
        save_user_enterprise(user_id, username, full_name)
        
        chat_type = "𝑷𝒓𝒊𝒗𝒂𝒕𝒆 𝑪𝒉𝒂𝒕"
        if message.chat:
            if message.chat.type in ['group', 'supergroup']:
                chat_type = f"𝑮𝒓𝒐𝒖𝒑: {message.chat.title}"
            elif message.chat.type == 'channel':
                chat_type = f"𝑪𝒉𝒂𝒏𝒏𝒆𝒍: {message.chat.title}"
        
        req_number = get_next_request_count() if "Command" in source_action else "𝑵/𝑨"
        current_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=5)).strftime("%d %b %Y, %I:%M %p")
        
        log_msg = (
            f"🔥☠️ 𝐌.𝐊 𝐇𝐀𝐂𝐊𝐄𝐑 — 𝐃𝐀𝐓𝐀 𝐋𝐎𝐆 𝐒𝐘𝐒𝐓𝐄𝐌 ☠️🔥\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"🤖 𝐁𝐨𝐭 𝐍𝐚𝐦𝐞: {BOT_NAME}\n"
            f"👑 𝐁𝐫𝐚𝐧𝐝: {BRAND_NAME}\n"
            f"🆔 𝐔𝐬𝐞𝐫 𝐈𝐃: {user_id}\n"
            f"👤 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: {username}\n"
            f"📛 𝐍𝐚𝐦𝐞: {full_name}\n"
            f"💬 𝐈𝐧𝐭𝐞𝐫𝐚𝐜𝐭𝐢𝐨𝐧: {chat_type}\n"
            f"📊 𝐀𝐜𝐭𝐢𝐯𝐢𝐭𝐲 𝐂𝐨𝐮𝐧𝐭: #{req_number}\n"
            f"🛡️ 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐒𝐭𝐚𝐭𝐮𝐬: Secured & Verified ✅\n"
            f"🕐 𝐓𝐢𝐦𝐞: {current_time}\n"
            f"📱 𝐀𝐜𝐭𝐢𝐨𝐧 𝐒𝐨𝐮𝐫𝐜𝐞: {source_action}\n"
            f"🔥 𝐁𝐨𝐭: {BOT_USERNAME} 𓆩☠𓆪\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )
        
        try:
            photos = bot.get_user_profile_photos(user_id=user_id, limit=1)
            if photos.total_count > 0:
                bot.send_photo(chat_id=LOG_CHANNEL_ID, photo=photos.photos[0][-1].file_id, caption=log_msg)
                return
        except Exception:
            pass

        bot.send_message(chat_id=LOG_CHANNEL_ID, text=log_msg + "\n\n⚠️ 𝐔𝐒𝐄𝐑 𝐇𝐀𝐒 𝐍𝐎 𝐏𝐑𝐎𝐅𝐈𝐋𝐄 𝐏𝐇𝐎𝐓𝐎 𝜌️")
    except Exception as e:
        print(f"Log error: {e}")

# ==========================================
# 🤖 HANDLERS & EDIT MESSAGE NAVIGATION
# ==========================================
@bot.message_handler(commands=["start"])
def send_welcome(message):
    send_data_to_log_channel(message, "Bot /start Command")
    user_id = message.from_user.id
    user_name = message.from_user.first_name if message.from_user.first_name else "User"

    if not verify_user_membership(user_id):
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_join = types.InlineKeyboardButton("📢 𝐉𝐎𝐈𝐍 😈☠️ 𝐌.𝐊 𝐇𝐀𝐂𝐊𝐄𝐑 ☠️😈 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=CHANNEL_INVITE_LINK)
        btn_check = types.InlineKeyboardButton("✅ 𝐉𝐎𝐈𝐍𝐄𝐃 / 𝐂𝐎𝐍𝐅𝐈𝐑𝐌", callback_data="check_join")
        btn_contact = types.InlineKeyboardButton("💬 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 😈☠️ 𝗠.𝗞 𝗛𝗔𝐂𝐊𝗘𝗥 ☠️😈 𝐎𝐖𝐍𝐄𝐑 👑", url=OWNER_CONTACT)
        markup.add(btn_join, btn_check, btn_contact)

        bot.send_message(
            message.chat.id,
            f"👋 𝐇𝐞𝐥𝐥𝐨 {user_name}!\n\n"
            f"🚨 𝐒𝐘𝐒𝐓𝐄𝐌 𝐀𝐂𝐂𝐄𝐒𝐒 𝐑𝐄𝐒𝐓𝐑𝐈𝐂𝐓𝐄𝐃\n\n"
            f"🔐 𝐉𝐨𝐢𝐧 𝐨𝐮𝐫 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐭𝐨 𝐮𝐧𝐥𝐨𝐜𝐤 𝐛𝐨𝐭 𝐚𝐜𝐜𝐞𝐬𝐬.\n\n"
            f"📌 𝐀𝐟𝐭𝐞𝐫 𝐣𝐨𝐢𝐧𝐢𝐧𝐠, 𝐜𝐥𝐢𝐜𝐤:\n"
            f"✅ 𝐉𝐎𝐈𝐍𝐄𝐃 / 𝐂𝐎𝐍𝐅𝐈𝐑𝐌",
            reply_markup=markup,
            parse_mode="Markdown",
        )
        return

    show_main_menu(message.chat.id, user_name, message_id=None)

@bot.message_handler(commands=["channel"])
def channel_command(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("📢 𝐉𝐎𝐈𝐍 😈☠️ 𝐌.𝐊 𝐇𝐀𝐂𝐊𝐄𝐑 ☠️😈 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=CHANNEL_INVITE_LINK)
    markup.add(btn)
    bot.send_message(
        message.chat.id,
        "📢 **😈☠️ 𝗠.𝗞 𝗛𝗔𝗖𝗞𝗘𝗥 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ☠️😈**\n\n"
        "✨ **𝐒𝐭𝐚𝐲 𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐞𝐝 • 𝐒𝐭𝐚𝐲 𝐔𝐩𝐝𝐚𝐭𝐞𝐝**\n\n"
        "🔥 𝐆𝐞𝐭 𝐭𝐡𝐞 𝐋𝐚𝐭𝐞𝐬𝐭 𝐔𝐩𝐝𝐚𝐭𝐞𝐬, 𝐍𝐞𝐰 𝐁𝐨𝐭 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬, "
        "𝐀𝐧𝐧𝐨𝐮𝐧𝐜𝐞𝐦𝐞𝐧𝐭𝐬, 𝐚𝐧𝐝 𝐄𝐱𝐜𝐥𝐮𝐬𝐢𝐯𝐞 𝐑𝐞𝐥𝐞𝐚𝐬𝐞𝐬 "
        "𝐟𝐫𝐨𝐦 𝐌.𝐊 𝐇𝐀𝐂𝐊𝐄𝐑.\n\n"
        "👇 **𝐓𝐚𝐩 𝐭𝐡𝐞 𝐁𝐮𝐭𝐭𝐨𝐧 𝐁𝐞𝐥𝐨𝐰 𝐭𝐨 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥 𝐂𝐇𝐀𝐍𝐍𝐄𝐋!**",
        reply_markup=markup,
        parse_mode="Markdown"
    )

@bot.message_handler(commands=["contact"])
def contact_command(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("💬 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 😈☠️ 𝗠.𝗞 𝗛𝐀𝐂𝐊𝗘𝗥 ☠️😈 𝐎𝐖𝐍𝐄𝐑 👑", url=OWNER_CONTACT)
    markup.add(btn)
    bot.send_message(
        message.chat.id,
        "💬 **𝐂𝐎𝐍𝐓𝐀𝐂𝐓 😈☠️ 𝗠.𝗞 𝗛𝐀𝐂𝐊𝐄𝗥 ☠️😈 𝐎𝐖𝐍𝐄𝐑 👑**\n\n"
        "⚡ **𝐍𝐞𝐞𝐝 𝐇𝐞𝐥𝐩, 𝐂𝐮𝐬𝐭𝐨𝐦 𝐁𝐨𝐭𝐬, 𝐨𝐫 𝐓𝐞𝐜𝐡𝐧𝐢𝐜𝐚𝐥 𝐒𝐮𝐩𝐩𝐨𝐫𝐭?**\n\n"
        "🤖 𝐆𝐞𝐭 𝐇𝐞𝐥𝐩 𝐖𝐢𝐭𝐡 𝐁𝐨𝐭 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐦𝐞𝐧𝐭, "
        "𝐂𝐮𝐬𝐭𝐨𝐦 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬, 𝐚𝐧𝐝 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐈𝐧𝐪𝐮𝐢𝐫𝐢𝐞𝐬.\n\n"
        "👑 **𝐃𝐢𝐫𝐞𝐜𝐭 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 • 𝐏𝐞𝐫𝐬𝐨𝐧𝐚𝐥𝐢𝐳𝐞𝐝 𝐒𝐮𝐩𝐩𝐨𝐫𝐭**\n\n"
        "👇 **𝐓𝐚𝐩 𝐭𝐡𝐞 𝐁𝐮𝐭𝐭𝐨𝐧 𝐁𝐞𝐥𝐨𝐰 𝐭𝐨 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐭𝐡𝐞 𝐎𝐰𝐧𝐞𝐫!**",
        reply_markup=markup,
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    user_id = call.from_user.id
    user_name = call.from_user.first_name if call.from_user.first_name else "User"
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    if call.data == "check_join":
        if verify_user_membership(user_id):
            bot.answer_callback_query(call.id, "✅ Access Granted! Welcome.")
            try:
                bot.delete_message(chat_id, message_id)
            except Exception:
                pass
            show_main_menu(chat_id, user_name, message_id=None)
        else:
            bot.answer_callback_query(call.id, "❌ Aapne abhi tak channel join nahi kiya!", show_alert=True)

    elif call.data == "main_menu":
        bot.answer_callback_query(call.id)
        show_main_menu(chat_id, user_name, message_id=message_id)

    elif call.data == "my_account":
        bot.answer_callback_query(call.id)
        joined_date, status, conv_count = get_user_profile_data(user_id)
        acc_text = (
            f"😈☠️ 𝑴.𝑲 𝑯𝑨𝑪𝑲𝑬𝑹 ☠️😈\n"
            f"💎 **𝓥𝑰𝓞 𝓟𝑹𝑶𝑭𝑰𝑳𝑬 𝑫𝑨𝑺𝑯𝑩𝑶𝑨𝑹𝑫** 💎\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"🆔 **𝐔𝐬𝐞𝐫 𝐈𝐃:** `{user_id}`\n"
            f"📛 **𝐅𝐮𝐥𝐥 𝐍𝐚𝐦𝐞:** {user_name}\n"
            f"📅 **𝐑𝐞𝐠𝐢𝐬𝐭𝐫𝐚𝐭𝐢𝐨𝐧:** {joined_date}\n"
            f"⚡ **𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐞𝐝 𝐓𝐞𝐱𝐭𝐬:** `{conv_count}`\n"
            f"💎 **𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐒𝐭𝐚𝐭𝐮𝐬:** `{status}` ✅\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"🔥 **𝒀𝑶𝑼𝑹 𝑨𝑪𝑪𝑶𝑼𝑵𝑻. 𝒀𝑶𝑼𝑹 𝑺𝑻𝑨𝑻𝑺.**\n"
            f"😈☠️ 𝑴.𝑲 𝑯𝑨𝑪𝑲𝑬𝑹 ☠️😈"
        )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("𝓡ℯ𝓉𝓊𝓇𝓃 𝓉ℴ 𝓜𝒶𝒾𝓃 𝓜ℯ𝓃𝓊", callback_data="main_menu"))
        try:
            bot.edit_message_text(acc_text, chat_id, message_id, reply_markup=markup, parse_mode="Markdown")
        except Exception:
            bot.send_message(chat_id, acc_text, reply_markup=markup, parse_mode="Markdown")

    elif call.data == "saved_fonts":
        bot.answer_callback_query(call.id)
        bookmarks = get_user_bookmarks(user_id)
        if not bookmarks:
            txt = (
                f"💾 **𝒮𝒶𝓋ℯ𝒹 ℱℴ𝓃𝓉𝓈**\n"
                f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"📚 **𝒀𝑶𝑼𝑹 𝑷𝑬𝑹𝑺𝑶𝑵𝑨𝑳 𝑭𝑶𝑵𝑻 𝑪𝑶𝑳𝑳𝑬𝑪𝑻𝑰𝑶𝑵**\n\n"
                f"❌ **𝑵𝑶 𝑺𝑨𝑽𝑬𝑫 𝑭𝑶𝑵𝑻𝑺 𝒀𝑬𝑻!**\n\n"
                f"💡 Save your favourite font styles here for quick access.\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━━\n"
                f"😈☠️ 𝑴.𝑲 𝑯𝑨𝑪𝑲𝑬𝑹 ☠️😈"
            )
        else:
            txt = f"💾 **𝒮𝒶𝓋ℯ𝒹 ℱℴ𝓃𝓉𝓈**\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
            for name, sample, dt in bookmarks:
                txt += f"▪️ **{name}** ({dt}):\n`{sample}`\n\n"
            txt += f"━━━━━━━━━━━━━━━━━━━━━━\n😈☠️ 𝑴.𝑲 𝑯𝑨𝑪𝑲𝑬𝑹 ☠️😈"
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("𝓡ℯ𝓉𝓊𝓇𝓃 𝓉ℴ 𝓜𝒶𝒾𝓃 𝓜ℯ𝓃𝓊", callback_data="main_menu"))
        try:
            bot.edit_message_text(txt, chat_id, message_id, reply_markup=markup, parse_mode="Markdown")
        except Exception:
            bot.send_message(chat_id, txt, reply_markup=markup, parse_mode="Markdown")

    elif call.data == "history_logs":
        bot.answer_callback_query(call.id)
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT action_type, payload, timestamp FROM activity_history WHERE user_id = ? ORDER BY id DESC LIMIT 10", (user_id,))
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            txt = (
                f"📜 **ℋ𝒾𝓈𝓉ℴ𝓇𝓎 ℒℴℊ𝓈**\n"
                f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"📂 **𝒀𝑶𝑼𝑹 𝑨𝑪𝑻𝑰𝑽𝑰𝑻𝒀 𝑹𝑬𝑷𝑶𝑹𝑻**\n\n"
                f"❌ **𝑵𝑶 𝑨𝑪𝑻𝑰𝑽𝑰𝑻𝒀 𝑭𝑶𝑼𝑵𝑫!**\n\n"
                f"📝 Your activity history is empty.\n"
                f"✨ Start using the bot to build your history!\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━━\n"
                f"😈☠️ 𝑴.𝑲 𝑯𝑨𝑪𝑲𝑬𝑹 ☠️😈"
            )
        else:
            txt = f"📜 **ℋ𝒾𝓈𝓉ℴ𝓇𝓎 ℒℴℊ𝓈**\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
            for act, payload, ts in rows:
                txt += f"🔹 **{act}** [{ts}]:\n`{payload}`\n\n"
            txt += f"━━━━━━━━━━━━━━━━━━━━━━\n😈☠️ 𝑴.𝑲 𝑯𝑨𝑪𝑲𝑬𝑹 ☠️😈"

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("𝓡ℯ𝓉𝓊𝓇𝓃 𝓉ℴ 𝓜𝒶𝒾𝓃 𝓜ℯ𝓃𝓊", callback_data="main_menu"))
        try:
            bot.edit_message_text(txt, chat_id, message_id, reply_markup=markup, parse_mode="Markdown")
        except Exception:
            bot.send_message(chat_id, txt, reply_markup=markup, parse_mode="Markdown")

    elif call.data.startswith("bookmark_save_"):
        bot.answer_callback_query(call.id, "💾 Font successfully saved to your VIP Bookmarks!", show_alert=True)

    elif call.data in FONTS:
        font_name = FONTS[call.data]["name"]
        user_state[user_id] = {
            "state": "waiting_for_text",
            "selected_font": call.data,
        }
        bot.answer_callback_query(call.id)
        bot.send_message(
            chat_id,
            f"✍ *Selected Style:* `{font_name}`\n\nAb apna normal text yahan send karein convert karne ke liye:",
            parse_mode="Markdown",
        )

def show_main_menu(chat_id, user_name, message_id=None):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    btn_acc = types.InlineKeyboardButton("My Account", callback_data="my_account")
    btn_saved = types.InlineKeyboardButton("Saved Fonts", callback_data="saved_fonts")
    btn_hist = types.InlineKeyboardButton("History Logs", callback_data="history_logs")
    btn_contact = types.InlineKeyboardButton("💬 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐎𝐖𝐍𝐄𝐑 👑", url=OWNER_CONTACT)
    
    markup.add(btn_acc, btn_saved)
    markup.add(btn_hist, btn_contact)

    font_buttons = []
    for key, data in FONTS.items():
        font_buttons.append(
            types.InlineKeyboardButton(f"✨ {data['name']}", callback_data=key)
        )
    markup.add(*font_buttons)

    menu_text = (
        f"⚡️ 😈☠️ 𝑴.𝑲 𝑯𝑨𝑪𝑲𝑬𝑹 ☠️😈 ⚡️\n"
        f"👑 𝑽𝑰𝑷 𝑭𝑶𝑵𝑻 𝑮𝑬𝑵𝑬𝑹𝑨𝑻𝑶𝑹 𝑷𝑹𝑶 👑\n\n"
        f"👋 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑩𝒂𝒄𝒌, {user_name}!\n"
        f"💎 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑺𝒆𝒓𝒊𝒇 𝑭𝒐𝒏𝒕 𝑮𝒆𝒏𝒆𝒓𝒂𝒕𝒐𝒓 𝑰𝒔 𝑹𝒆𝒂𝒅𝒚.\n\n"
        f"🟢 𝑺𝒀𝑺𝑻𝑬𝑴: 𝑶𝑵𝑳𝑰𝑵𝑬  |  👑 𝑴𝑶𝑫𝑬: 𝑽𝑰𝑷\n\n"
        f"🎨 𝒮ℯ𝓁ℯ𝒸𝓉 𝒴ℴ𝓊𝓇 ℱ𝒶𝓋ℴ𝓊𝓇𝒾𝓉ℯ 𝒮ℯ𝓇𝒾𝒻 𝒮𝓉𝓎𝓁ℯ 👇"
    )

    if message_id:
        try:
            bot.edit_message_text(menu_text, chat_id, message_id, reply_markup=markup, parse_mode="Markdown")
            return
        except Exception:
            pass
    bot.send_message(chat_id, menu_text, reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(
    func=lambda message: isinstance(user_state.get(message.from_user.id), dict)
    and user_state.get(message.from_user.id).get("state") == "waiting_for_text"
)
def generate_font_text(message):
    user_id = message.from_user.id
    user_data = user_state.get(user_id)
    font_key = user_data["selected_font"]
    font_name = FONTS[font_key]["name"]
    input_text = message.text

    converted_text = apply_font(input_text, font_key)
    
    log_activity_enterprise(user_id, f"Generated: {font_name}", converted_text[:35])
    save_font_bookmark(user_id, font_name, converted_text)

    response = (
        f"🔥 *Generated with {font_name}* 🔥\n\n"
        f"`{converted_text}`\n\n"
        f"👑 *Branded By:* [{BRAND_NAME}]({OWNER_CONTACT})"
    )

    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("💾 𝒮𝒶𝓋ℯ ℬℴℴ𝓀𝓂𝒶𝓇𝓀", callback_data=f"bookmark_save_{font_key}"),
        types.InlineKeyboardButton("𝓡ℯ𝓉𝓊𝓇𝓃 𝓉ℴ 𝓜𝒶𝒾𝓃 𝓜ℯ𝓃𝓊", callback_data="main_menu")
    )

    user_state[user_id] = None
    bot.send_message(
        message.chat.id,
        response,
        reply_markup=markup,
        parse_mode="Markdown",
        disable_web_page_preview=True,
    )

# ==========================================
# 📢 BROADCAST CHANNEL POST FORWARDER
# ==========================================
@bot.channel_post_handler(func=lambda message: str(message.chat.id) == str(BROADCAST_CHANNEL_ID))
def broadcast_posts(message):
    try:
        users = get_all_registered_users()
        for uid in users:
            try:
                bot.copy_message(
                    chat_id=uid,
                    from_chat_id=message.chat.id,
                    message_id=message.message_id
                )
            except Exception as ex:
                print(f"Forward error to user {uid}: {ex}")
    except Exception as e:
        print(f"Broadcast handler error: {e}")

# Vercel Serverless Webhook Handler
class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            json_data = json.loads(post_data.decode('utf-8'))
            update = telebot.types.Update.de_json(json_data)
            bot.process_new_updates([update])

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
        except Exception as e:
            print(f"Webhook error: {e}")
            self.send_response(500)
            self.end_headers()

    def do_GET(self):
        self.send_range_response = 200
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"M.K HACKER Serif Font, Log & Broadcast Bot is active on Vercel!")
