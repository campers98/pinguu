import importlib
import logging
from telegram import Update
from chatbot import rani
from chatbot.modules import ALL_MODULES


def main():
    rani.run_polling(
        timeout=15,
        drop_pending_updates=False,
        allowed_updates=Update.ALL_TYPES,
        stop_signals=None,
    )


FORMAT = "[INFO] %(message)s"

if __name__ == "__main__":
    logging.basicConfig(
        handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
        level=logging.INFO,
        format=FORMAT,
        datefmt="[%X]",
    )
    logging.getLogger("ptbcontrib.postgres_persistence.postgrespersistence").setLevel(
        logging.INFO
    )
    for module in ALL_MODULES:
        importlib.import_module("chatbot.modules." + module)
    main()
    print("ɪ ᴀᴍ ɴᴏᴡ ᴏɴʟɪɴᴇ")
