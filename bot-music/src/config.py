# /src/config.py
import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "app": {
        "token": os.getenv("DISCORD_TOKEN"),
        "playing": "by BOT NAME ❤️",
        "global": True,
        "guild": os.getenv("GUILD"),
        "extraMessages": False,
        "loopMessage": False,
        "lang": "en",
        "enableEmojis": False,
    },
    "emojis": {
        "back": "⏪",
        "skip": "⏩",
        "ResumePause": "⏯️",
        "volumeUp": "🔊",
        "volumeDown": "🔉",
        "loop": "🔁",
        "music": "🎵",
    },
    "opt": {
        "DJ": {"enabled": False, "roleName": "", "commands": []},
        "maxVol": 200,
        "spotifyBridge": True,
        "volume": 100,
        "leaveOnEmpty": True,
        "leaveOnEmptyCooldown": 30000,
        "leaveOnEnd": True,
        "leaveOnEndCooldown": 30000,
        "discordPlayer": {
            "YoutubeiExtractor": {"quality": "highestaudio", "highWaterMark": 1 << 25}
        },
    },
}
