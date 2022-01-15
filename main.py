import telepot as tp
import time as t

bot = tp.Bot("1963378791:AAF_IQiZDk_rGT6bvwSzGzCGegBxdQeUBqs")

def chat(msg):
    content_type, chat_type, chat_id = tp.glance(msg)

    if content_type == "text":
        if msg["text"] == "/set":
            bot.sendMessage(chat_id )

bot.message_loop(chat)

while True:
    t.sleep(5)