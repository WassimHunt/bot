import telebot
import os
os.system("rm -f EMAILS.txt")
import requests,random
from telebot import types
import user_agent
from user_agent import generate_user_agent
bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=["start"])
def s(message):
    try:
        user = message.from_user.username
        nam = message.chat.first_name
        dev = types.InlineKeyboardButton(text="7🅰️🅼🅾️🅳🆈", url="https://t.me/egy_p_t")
        key = types.InlineKeyboardMarkup()
        key.add(dev)
        uu = f"https://t.me/{user}"
        bot.send_photo(message.chat.id, uu,f"""
ᯓ HI {nam} Welcome Bot @EGY_P_T
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ BOT CHECK COIN INSTA UP
ᯓ SEND FILE ID
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
By : @EGY_P_T - Tele : @H_AMO_DY""", reply_markup=key)
    except:
        name = message.chat.first_name
        dev = types.InlineKeyboardButton(text="7🅰️🅼🅾️🅳🆈", url="https://t.me/egy_p_t")
        key = types.InlineKeyboardMarkup()
        key.add(dev)
        bot.send_message(message.chat.id, f"""
ᯓ HI {name} Welcome Bot @EGY_P_T
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ BOT CHECK EMAIL FACEBOOK
ᯓ SEND FILE EMAIL
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
By : @EGY_P_T - Tele : @H_AMO_DY""", reply_markup=key)
@bot.message_handler(func=lambda m:True)
def f(message):
    if ":" in message.text:
        id = message.text.split(":")[0]
        pk = message.text.split(":")[1]
        req = requests.get(
            f"http://send.ramzinetflix.repl.co/?target={pk}&userid={id}&submit=submit").text
        if "Sending orders less than 110 is temporarily disabled. Please try again in another hour." in req:
            bot.send_message(message.chat.id, f"There Is arequest under review ⛔️\nYOUR ID : {id}\nID PK : {pk}")
        if "Your accound suspended due to unfollowing. If you think there is a mistake, call us at instaup.developers@gmail.com." in req:
            bot.send_message(message.chat.id, f"Account Blocked ❌\nYOUR ID : {id}\nID PK : {pk}")
        if "DONE" in req:
            print(req)
            coin = req.split("DONE : ")[1].split("<hr>")[0]
            bot.send_message(message.chat.id, f"[✅]Successful Send {id}\nFollowers : {coin}")
        if "Successful" in req:
            coin = req.split("DONE  : ")[1].split("<hr>")[0]
            bot.send_message(message.chat.id, f"[✅]Successful Send {id}\nFollowers : {coin}")
        if "You don't have enough coins!" in req:
            bot.send_message(message.chat.id, f"Less Coins ❌\nYOUR ID : {id}\nIS PK : {pk}")
@bot.message_handler(content_types=['document'])
def send_file(message):
    file_input = bot.download_file(bot.get_file(message.document.file_id).file_path)
    with open(f"EMAILS.txt","wb") as file:
        file.write(file_input)
    start = bot.send_message(message.chat.id,f"START ▶️")
    mn=0
    for hamody in open("EMAILS.txt","r").read().splitlines():
        userid = hamody.split("\n")[0]
        url = 'https://check.ramzinetflix.repl.co/?oid={}&submit=submit'.format(userid)
        headers = {
            'Host': 'https://check.ramzinetflix.repl.co',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': 'Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'X-Chrome-offline': 'persist=0 reason=reload',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': str(generate_user_agent()),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Encoding': 'gzip',
            'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7'}
        responsa = requests.get(url, headers).text

        if ('main') in responsa:
            check = types.InlineKeyboardButton(text=f"ID ⚜️ : {userid}", callback_data="snsj")
            emails = types.InlineKeyboardButton(text=f"COIN 💵  : BANNED ⚠️", callback_data="dj")
            key = types.InlineKeyboardMarkup()
            key.add(emails)
            key.add(check)
            name = message.chat.first_name
            bot.edit_message_text(
                text=f"""
ᯓ HI {name}
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ Please wait for the check.
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
By : @EGY_P_T - Tele : @H_AMO_DY""",
                chat_id=message.chat.id, message_id=start.message_id, reply_markup=key)
        elif ('{"coins":') in responsa:
            coinx = str(responsa.split('coins":"')[1])
            coin = str(coinx.split('"')[0])
            if int(coin) > 400:
                bot.send_message(message.chat.id,f"""
ᯓ NEW ID ✅
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ ID : <code>{userid}</code>
ᯓ COIN 💵 : {coin}
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
By : @EGY_P_T - Tele : @H_AMO_DY""",parse_mode="html")
            else:
                check = types.InlineKeyboardButton(text=f"ID ⚜️ : {userid}", callback_data="snsj")
                emails = types.InlineKeyboardButton(text=f"COIN 💵 : {coin}", callback_data="dj")
                key = types.InlineKeyboardMarkup()
                key.add(emails)
                key.add(check)
                name = message.chat.first_name
                bot.edit_message_text(
                    text=f"""
ᯓ HI {name}
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ Please wait for the check.
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
By : @EGY_P_T - Tele : @H_AMO_DY""",
                    chat_id=message.chat.id, message_id=start.message_id, reply_markup=key)
        else:
            check = types.InlineKeyboardButton(text=f"ID ⚜️ : {userid}", callback_data="snsj")
            emails = types.InlineKeyboardButton(text=f"COIN 💵 : BANNED ⚠️", callback_data="dj")
            key = types.InlineKeyboardMarkup()
            key.add(emails)
            key.add(check)
            name = message.chat.first_name
            bot.edit_message_text(
                text=f"""
ᯓ HI {name}
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ Please wait for the check.
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
By : @EGY_P_T - Tele : @H_AMO_DY""",
                chat_id=message.chat.id, message_id=start.message_id, reply_markup=key)
bot.polling()




@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://botsendf.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
