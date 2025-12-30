import random

def get_reply(text, name):
    text = text.lower()

    deny_words = ["bot", "robot", "ai", "artificial", "program", "script", "coded"]

    if any(word in text for word in deny_words):
        replies = [
            f"Yeno {name} 😂 naan bot alla guru 😎",
            f"Ayyo {name} 🤣 sumne kelbeda!",
            f"Naan manushya guru 😏 chill maadu",
        ]
        return random.choice(replies)

    if "hi" in text or "hello" in text:
        return f"Hi {name} 😄 En samachaara?"

    if "how are you" in text:
        return f"Naan super maga 😎 Nee hegidya?"

    if "who are you" in text:
        return f"Naan nin friend maga 😁🔥"

    if "love" in text:
        return f"Ayyoo 😳 full feels-u guru ❤️😂"

    if "bye" in text:
        return f"Bye {name} 👋 Jaldi sigona 😄"

    casual = [
        f"{name} 😄 chill maadu guru",
        f"Yeno scene illa {name} 😎",
        f"Cool ah iru {name} 🔥",
    ]

    return random.choice(casual)
