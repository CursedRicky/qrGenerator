import telepot as tp
import time as t

bot = tp.Bot("1963378791:AAF_IQiZDk_rGT6bvwSzGzCGegBxdQeUBqs")

def chat(msg):
    content_type, chat_type, chat_id = tp.glance(msg)

    if content_type == "text":
        if msg["text"] == "/set cod1":
            f = open('order.txt', 'a')
            bot.sendMessage(chat_id, "aggiunto cod1 al tuo ordine")
            f.write(f"{chat_id} cod1\n")
            f.close()

bot.message_loop(chat)

while True:
    t.sleep(5)