import telepot as tp
import time as t
import qrcode as qr

bot = tp.Bot("TOKEN")

def chat(msg):
    content_type, chat_type, chat_id = tp.glance(msg)

    if content_type == "text":
        img = qr.make(msg["text"])
        img.save("code.png")
        bot.send_photo(chat_id, photo=open('.code.png', 'rb'))
        # if msg["text"] == "Ciao":
        #     bot.sendMessage(chat_id, "Ciao")

bot.message_loop(chat)

while True:
    t.sleep(5)
