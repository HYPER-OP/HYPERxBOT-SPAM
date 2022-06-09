import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import xd, xd2, xd3, xd4, xd5, xd6, xd7, xd8, xd9, xd10, ALIVE_PIC, OWNER_ID
from xdoeLXSpam.plugins.help import *


xd_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/c3d7807b02a4c1d039f12.jpg"

xd_Button = [
        [
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/CHATROOM_XD")
        ],
        [
        Button.inline("• ᴄᴍᴅs •", data="help_back")
        ]
        ]
               
HYPX_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/CHATROOM_XD"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/CHATROOM_XD")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/HYPER-OP/")
        ]
        ]
        
        
#USERS 


@xd.on(events.NewMessage(pattern="/start"))
@xd2.on(events.NewMessage(pattern="/start"))
@xd3.on(events.NewMessage(pattern="/start"))
@xd4.on(events.NewMessage(pattern="/start"))
@xd5.on(events.NewMessage(pattern="/start"))
@xd6.on(events.NewMessage(pattern="/start"))
@xd7.on(events.NewMessage(pattern="/start"))
@xd7.on(events.NewMessage(pattern="/start"))
@xd8.on(events.NewMessage(pattern="/start"))
@xd9.on(events.NewMessage(pattern="/start"))
@xd10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       xdBot = await event.client.get_me()
       bot_id = xdBot.first_name
       bot_username = xdBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       HYPER = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hi Master, Its me {bot_id}, Your Spam Bot !! \n\n Click Below Buttons For help**"
       usermsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [ʜʏᴘᴇʀ ✗ sᴘᴀᴍ](https://t.me/CHATROOM_XD)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(HYPER,
                  xd_IMG,
                  caption=ownermsg, 
                  buttons=xd_Button)
       else:
            await event.client.send_file(HYPER,
                  xd_IMG,
                  caption=usermsg, 
                  buttons=HYPX_Button)
                

