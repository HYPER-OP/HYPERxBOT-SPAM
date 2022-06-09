from HYPERxSpam import xd, xd2, xd3, xd4, xd5, xd6, xd7, xd8, xd9, xd10, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from HYPERxSpam import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/7ebd8c5c6566b8e18de27.jpg"

xd_Help = "__Click On Below Buttons for help__"


@xd.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@xd2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@xd3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@xd4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@xd5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@xd6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@xd7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@xd8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@xd9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@xd10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=xd_Help,
                                  buttons=[
           [
            Button.inline("• Spam •", data="spam"),
            Button.inline("• Raid •", data="raid"),
           ],
           [
            Button.inline("• Extra •", data="extra"),
           ],
           [    
            Button.url("JOIN", "https://t.me/CHATROOM_XD")
           ],
           ],
           )              

  
  
extra_msg = f"""
**Help Extra Cmds**

**Userbot**: Userbot Cmds
command:
i) {hl}ping 
ii) {hl}alive
iii) {hl}restart
iv) {hl}addsudo <reply to user> : Owner Cmd

**Echo**: To Active Echo On Any User
command:
i) {hl}addecho <reply to user>
ii) {hl}rmecho <reply to user>

**Leave**: To Leave Group/channel
command:
i) {hl}leave <group/chat id>
ii) {hl}leave : Type in the Group bot will auto leave that group

**Packspam**: Sticker Pack Spam
i) {hl}packspam (replying to any sticker)

**© @CHATROOM_XD**
"""

                 
raid_msg = f"""
**Help Raid Cmds**


**raid:** Activates raid on any individual user for given range.
command:
i) {hl}raid <count> <username
ii) {hl}raid <count> <reply to user>

**Delayraid**: Activates raid on any individual user for given range.
Command:
i) {hl}delayraid <delay> <count> <Username of User>
ii) {hl}delayraid <delay> <count> <reply to a User>

**replyraid:** Activates Reply Raid on the user!!
command:
i) {hl}replyraid <replying to user>
ii) {hl}dreplyraid <username>

**dreplyraid:** Deactivates reply raid on the user!!
command:
i) {hl}dreplyraid <replying to user>
ii) {hl}dreplyraid <username>


**© @CHATROOM_XD**
"""

spam_msg = f"""
**Help Spam Cmds**

**spam**: Spams a message for given counter(<= 100).
command:
i) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}spam <count> <replying any message>

**bigspam**: Spams a message for given counter.
command:
i) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}bigspam <count> <replying any message>

**delayspam**: Delay spam a text for given counter after given time.
command:
i) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}delayspam <delay> <count> <replying any message>

**pornspam**: Pornography Spam.
command:
i) {hl}pornspam <count>

**hang**: Spams hanging message for given counter.
command:
i) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

** © @CHATROOM_XD**
"""                     
           
           
@xd.on(events.CallbackQuery(pattern=r"help_back"))
@xd2.on(events.CallbackQuery(pattern=r"help_back"))
@xd3.on(events.CallbackQuery(pattern=r"help_back"))
@xd4.on(events.CallbackQuery(pattern=r"help_back"))
@xd5.on(events.CallbackQuery(pattern=r"help_back"))
@xd6.on(events.CallbackQuery(pattern=r"help_back"))
@xd7.on(events.CallbackQuery(pattern=r"help_back"))
@xd8.on(events.CallbackQuery(pattern=r"help_back"))
@xd9.on(events.CallbackQuery(pattern=r"help_back"))
@xd10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            xd_Help,
            buttons=[
                [
            Button.inline("Spam", data="spam"),
            Button.inline("Raid", data="raid"),
           ],
           [
            Button.inline("Extra cmds", data="extra"),
           ],
           [    
            Button.url("JOIN", "https://t.me/CHATROOM_XD")
           ],
           ],
        )           
   else:
        Alert = (
                "Noob !! Make Your Own ʜʏᴘᴇʀ ✗ sᴘᴀᴍ Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@xd.on(events.CallbackQuery(pattern=r"spam"))
@xd2.on(events.CallbackQuery(pattern=r"spam"))
@xd3.on(events.CallbackQuery(pattern=r"spam"))
@xd4.on(events.CallbackQuery(pattern=r"spam"))
@xd5.on(events.CallbackQuery(pattern=r"spam"))
@xd6.on(events.CallbackQuery(pattern=r"spam"))
@xd7.on(events.CallbackQuery(pattern=r"spam"))
@xd8.on(events.CallbackQuery(pattern=r"spam"))
@xd9.on(events.CallbackQuery(pattern=r"spam"))
@xd10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "Noob !! Make Your Own ʜʏᴘᴇʀ ✗ sᴘᴀᴍ Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@xd.on(events.CallbackQuery(pattern=r"raid"))
@xd2.on(events.CallbackQuery(pattern=r"raid"))
@xd3.on(events.CallbackQuery(pattern=r"raid"))
@xd4.on(events.CallbackQuery(pattern=r"raid"))
@xd5.on(events.CallbackQuery(pattern=r"raid"))
@xd6.on(events.CallbackQuery(pattern=r"raid"))
@xd7.on(events.CallbackQuery(pattern=r"raid"))
@xd8.on(events.CallbackQuery(pattern=r"raid"))
@xd9.on(events.CallbackQuery(pattern=r"raid"))
@xd10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "Noob !! Make Your Own ʜʏᴘᴇʀ ✗ sᴘᴀᴍ Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@xd.on(events.CallbackQuery(pattern=r"extra"))
@xd2.on(events.CallbackQuery(pattern=r"extra"))
@xd3.on(events.CallbackQuery(pattern=r"extra"))
@xd4.on(events.CallbackQuery(pattern=r"extra"))
@xd5.on(events.CallbackQuery(pattern=r"extra"))
@xd6.on(events.CallbackQuery(pattern=r"extra"))
@xd7.on(events.CallbackQuery(pattern=r"extra"))
@xd8.on(events.CallbackQuery(pattern=r"extra"))
@xd9.on(events.CallbackQuery(pattern=r"extra"))
@xd10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "Noob !! Make Your Own ʜʏᴘᴇʀ ✗ sᴘᴀᴍ Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)

