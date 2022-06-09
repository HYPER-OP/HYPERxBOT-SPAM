import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from xdoeLXSpam.utils import load_plugins
import logging
from telethon import events
from . import xd, xd2, xd3, xd4, xd5, xd6, xd7, xd8, xd9, xd10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "HYPERxSpam/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("HypeR Bot Spam Successfully deployed -!")
print("Enjoy! Do visit @CHATROOM_XD")

if __name__ == "__main__":
    xd.run_until_disconnected()
    
if __name__ == "__main__":
    xd2.run_until_disconnected()

if __name__ == "__main__":
    xd3.run_until_disconnected()
    
if __name__ == "__main__":
    xd4.run_until_disconnected()

if __name__ == "__main__":
    xd5.run_until_disconnected()
    
if __name__ == "__main__":
    xd6.run_until_disconnected()
    
if __name__ == "__main__":
    xd7.run_until_disconnected()

if __name__ == "__main__":
    xd8.run_until_disconnected()
    
if __name__ == "__main__":
    xd9.run_until_disconnected()

if __name__ == "__main__":
    xd10.run_until_disconnected()    
