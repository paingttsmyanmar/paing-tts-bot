import random
from telebot import TeleBot, types

# =========================================================
# ⚙️ Configuration
# =========================================================
BOT_TOKEN = "8547879121:AAE9zdWx5deE5VnhXp9k1yX_kfNh_dnClJc"
ADMIN_USERNAME = "trollmovie123"  # သင့် Telegram Username
BOT_USERNAME = "paing_tts_srt_bot"  # သင့် Bot ၏ Username (ရှေ့က @ မပါဘဲ)

bot = TeleBot(BOT_TOKEN)

# =========================================================
# 💬 Start ခလုတ်နှိပ်လျှင် (Private နှင့် Group ခွဲခြားခြင်း)
# =========================================================
@bot.message_handler(commands=['start'])
def welcome_message(message):
    # --- ၁။ User က Bot ရဲ့ Private Chat ထဲမှာ လာနှိပ်တာဆိုလျှင် ---
    if message.chat.type == 'private':
        # အောက်ခြေတွင် အမြဲပေါ်နေမည့် ခလုတ်ကြီး (၂) ခု
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_get_pass = types.KeyboardButton("🔑 Password ယူရန်")
        btn_web_link = types.KeyboardButton("🌐 ဆာဗာ Link")
        markup.add(btn_get_pass, btn_web_link)
        
        welcome_text = "👋 ဝင်ရောက်လာမှုကို ကြိုဆိုပါတယ်ဗျာ။ အသုံးပြုရန် အောက်ပါခလုတ်များမှတစ်ဆင့် ရွေးချယ်နိုင်ပါပြီ။ 👇"
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)
        
    # --- ၂။ Group ထဲမှာ /start လာနှိပ်တာဆိုလျှင် (PIN တင်ရန်အတွက် စာသားနှင့် ခလုတ်ထုတ်ပေးမည်) ---
    else:
        inline_markup = types.InlineKeyboardMarkup()
        # 🚨 နှိပ်လိုက်သည်နှင့် Bot ၏ Private Chat (Inbox) သို့ ချက်ချင်း ခေါ်သွားပေးမည့် ခလုတ်
        btn_go_private = types.InlineKeyboardButton("🔑 ဤနေရာကိုနှိပ်၍ သီးသန့် Password ယူပါ", url=f"https://t.me/{BOT_USERNAME}?start=get_password")
        inline_markup.add(btn_go_private)
        
        group_text = (
            "👑 **Myanmar TTS & SRT Premium Service** 👑\n\n"
            "ဆော့ဖ်ဝဲလ် အသုံးပြုရန်အတွက် အောက်ပါခလုတ်ကိုနှိပ်၍ **Bot ၏ Inbox (သီးသန့် Chat) တွင်** Password ကို လုံခြုံစွာ ရယူနိုင်ပါပြီဗျာ။ 👇"
        )
        bot.send_message(message.chat.id, group_text, parse_mode="Markdown", reply_markup=inline_markup)

# =========================================================
# ⌨️ ခလုတ်တစ်ခုချင်းစီ၏ အလုပ်လုပ်ပုံများ (Private တွင်သာ အလုပ်လုပ်မည်)
# =========================================================
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.chat.type == 'private':
        user_id = message.chat.id
        
        # --- '🔑 Password ယူရန်' ခလုတ်နှိပ်လျှင် ---
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

        # --- '🌐 ဆာဗာ Link' ခလုတ်နှိပ်လျှင် ---
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
        
