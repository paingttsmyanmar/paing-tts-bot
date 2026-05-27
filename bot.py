import random
from telebot import TeleBot, types

# =========================================================
# ⚙️ Configuration
# =========================================================
BOT_TOKEN = "8547879121:AAE9zdWx5deE5VnhXp9k1yX_kfNh_dnClJc"
ADMIN_USERNAME = "trollmovie123"  # သင့် Telegram Username

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_get_pass = types.KeyboardButton("🔑 ဝင်ခွင့် Password ယူမည်")
    btn_web_link = types.KeyboardButton("🌐 Web App သို့သွားမည်")
    markup.add(btn_get_pass, btn_web_link)
    
    welcome_text = (
        "👋 မင်္ဂလာပါဗျာ! Myanmar TTS & SRT Premium Bot မှ ကြိုဆိုပါတယ်။\n\n"
        "ဆော့ဖ်ဝဲလ်ကို အသုံးပြုရန်အတွက် အောက်က '🔑 ဝင်ခွင့် Password ယူမည်' ခလုတ်ကိုနှိပ်၍ Password ထုတ်ယူပါဗျာ။ 👇"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    user_id = message.chat.id
    
    if message.text == "🔑 ဝင်ခွင့် Password ယူမည်":
        # 🎲 User တစ်ယောက်ချင်းစီအတွက် မထပ်နိုင်မယ့် Password ဂဏန်း ၆ လုံး ထုတ်ပေးခြင်း
        generated_password = random.randint(100000, 999999)
        
        info_text = (
            "🎫 **သင်၏ ဆော့ဖ်ဝဲလ်ဝင်ခွင့် အချက်အလက်များ** 🎫\n\n"
            "🔑 **ဝင်ခွင့် Password -** `{password}`\n"
            "🆔 **Telegram ID -** `{user_id}`\n\n"
            "⚠️ **အရေးကြီးညွှန်ကြားချက် -**\n"
            "အပေါ်က Password နှင့် Telegram ID ကို ဖိနှိပ်ပြီး ကူးယူ (Copy) ပါ။ ပြီးနောက် "
            "Premium VIP ရက်ဝယ်ယူရန်အတွက် **ငွေလွှဲပြေစာ (Screenshot)** နှင့်အတူ Admin ထံသို့ ပေးပို့၍ ရက်သတ်မှတ်ခိုင်းရပါမည်ဗျာ။\n\n"
            "*(Admin မှ VIP ရက် သတ်မှတ်ပေးပြီးမှသာ ဝဘ်ဆိုက်ထဲသို့ ဝင်ရောက်အသုံးပြုနိုင်မည် ဖြစ်ပါသည်)*"
        ).format(password=generated_password, user_id=user_id)
        
        inline_markup = types.InlineKeyboardMarkup()
        inline_btn = types.InlineKeyboardButton("🔥 Admin ထံသို့ အချက်အလက်နှင့် ပြေစာပို့ရန်", url=f"https://t.me/{ADMIN_USERNAME}")
        inline_markup.add(inline_btn)
        
        bot.send_message(message.chat.id, info_text, parse_mode="Markdown", reply_markup=inline_markup)

    elif message.text == "🌐 Web App သို့သွားမည်":
        inline_markup = types.InlineKeyboardMarkup()
        inline_btn = types.InlineKeyboardButton("🚀 Web App ဖွင့်မည်", url="https://paingttsmyanmar.onrender.com")
        inline_markup.add(inline_btn)
        bot.send_message(message.chat.id, "အောက်ကခလုတ်ကိုနှိပ်ပြီး App ထဲသို့ ဝင်ရောက်နိုင်ပါတယ်ဗျာ။", reply_markup=inline_markup)

if __name__ == "__main__":
    from flask import Flask
    app = Flask('')
    @app.route('/')
    def home(): return "VIP Request Bot is Running!"
    
    import threading
    def run_bot(): bot.infinity_polling()
    threading.Thread(target=run_bot).start()
    
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
