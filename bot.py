import random
from telebot import TeleBot, types

# =========================================================
# ⚙️ Configuration
# =========================================================
BOT_TOKEN = "8547879121:AAE9zdWx5deE5VnhXp9k1yX_kfNh_dnClJc"
ADMIN_USERNAME = "trollmovie123"  # သင့် Telegram Username

bot = TeleBot(BOT_TOKEN)

# =========================================================
# 🚀 Start ခလုတ်နှိပ်လျှင် ခလုတ် (၂) ခုတည်း သီးသန့်ပြသခြင်း
# =========================================================
@bot.message_handler(commands=['start'])
def welcome_message(message):
    # အောက်ခြေတွင် ပေါ်မည့် ခလုတ်ကြီး (၂) ခု တည်ဆောက်ခြင်း
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_get_pass = types.KeyboardButton("🔑 Password ယူရန်")
    btn_web_link = types.KeyboardButton("🌐 ဆာဗာ Link")
    markup.add(btn_get_pass, btn_web_link)
    
    welcome_text = "👋 ဝင်ရောက်လာမှုကို ကြိုဆိုပါတယ်ဗျာ။ အသုံးပြုရန် အောက်ပါခလုတ်များမှတစ်ဆင့် ရွေးချယ်နိုင်ပါပြီ။ 👇"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# =========================================================
# ⌨️ ခလုတ်တစ်ခုချင်းစီ၏ အလုပ်လုပ်ပုံများ
# =========================================================
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    user_id = message.chat.id
    
    # --- ၁။ Password ယူရန် ခလုတ်နှိပ်လျှင် ---
    if message.text == "🔑 Password ယူရန်":
        generated_password = random.randint(100000, 999999)
        
        info_text = (
            "🎫 **သင်၏ ဆော့ဖ်ဝဲလ်ဝင်ခွင့် အချက်အလက်များ** 🎫\n\n"
            "🔑 **ဝင်ခွင့် Password -** `{password}`\n"
            "🆔 **Telegram ID -** `{user_id}`\n\n"
            "⚠️ **ညွှန်ကြားချက် -**\n"
            "အပေါ်က Password နှင့် Telegram ID အား ကူးယူ (Copy) ပြီး၊ "
            "**ငွေလွှဲပြေစာ (Screenshot)** နှင့်အတူ Admin ထံသို့ ပေးပို့၍ ရက်သတ်မှတ်ခိုင်းပါဗျာ။"
        ).format(password=generated_password, user_id=user_id)
        
        inline_markup = types.InlineKeyboardMarkup()
        inline_btn = types.InlineKeyboardButton("🔥 Admin ထံသို့ အချက်အလက်နှင့် ပြေစာပို့ရန်", url=f"https://t.me/{ADMIN_USERNAME}")
        inline_markup.add(inline_btn)
        
        bot.send_message(message.chat.id, info_text, parse_mode="Markdown", reply_markup=inline_markup)

    # --- ၂။ ဆာဗာ Link ခလုတ်နှိပ်လျှင် ---
    elif message.text == "🌐 ဆာဗာ Link":
        inline_markup = types.InlineKeyboardMarkup()
        inline_btn = types.InlineKeyboardButton("🚀 Web App ကို ဖွင့်မည်", url="https://paingttsmyanmar.onrender.com")
        inline_markup.add(inline_btn)
        
        bot.send_message(message.chat.id, "အောက်ကခလုတ်ကိုနှိပ်ပြီး App ထဲသို့ ဝင်ရောက်နိုင်ပါတယ်ဗျာ။ 👇", reply_markup=inline_markup)

# =========================================================
# 🌐 Web Server မောင်းနှင်ခြင်း
# =========================================================
if __name__ == "__main__":
    from flask import Flask
    app = Flask('')
    @app.route('/')
    def home(): return "Bot is Running!"
    
    import threading
    def run_bot(): bot.infinity_polling()
    threading.Thread(target=run_bot).start()
    
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
        
