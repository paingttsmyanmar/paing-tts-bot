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
        inline_markup = types.InlineKeyboardMarkup(row_width=1)
        
        # 🔑 PASSWORD ရယူရန် ခလုတ်
        btn_get_pass = types.InlineKeyboardButton("🔑 PASSWORD ရယူရန်", callback_data="get_password_now")
        
        # 🆓 FREE သုံးရန် ခလုတ် (နှိပ်လိုက်တာနဲ့ စာလုံးရေ ၂၀၀၀ ကန့်သတ်ချက်ရှိတဲ့ ဝဘ်ဆိုက်ဆီ တန်းခေါ်သွားမည်)
        btn_free_server = types.InlineKeyboardButton("🆓 FREE အစမ်းသုံးရန် (စာလုံးရေ ၂၀၀၀ ကန့်သတ်ချက်)", url="https://paingttsmyanmar.onrender.com")
        
        inline_markup.add(btn_get_pass, btn_free_server)
        
        welcome_text = "📢 **Myanmar TTS SRT App မှ ကြိုဆိုပါတယ်ဗျာ။**\nအောက်ပါခလုတ်များမှတစ်ဆင့် သင်အသုံးပြုလိုသော စနစ်ကို ရွေးချယ်ပါ 👇"
        bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown", reply_markup=inline_markup)
        
    # --- ၂။ Group ထဲမှာ /start လာနှိပ်တာဆိုလျှင် ---
    else:
        inline_markup = types.InlineKeyboardMarkup()
        btn_go_private = types.InlineKeyboardButton("🔑 ဤနေရာကိုနှိပ်၍ သီးသန့် Password ယူပါ", url=f"https://t.me/{BOT_USERNAME}?start=get_password")
        inline_markup.add(btn_go_private)
        
        group_text = (
            "👑 **Myanmar TTS & SRT Premium Service** 👑\n\n"
            "ဆော့ဖ်ဝဲလ် အသုံးပြုရန်အတွက် အောက်ပါခလုတ်ကိုနှိပ်၍ **Bot ၏ Inbox (သီးသန့် Chat) တွင်** Password ကို လုံခြုံစွာ ရယူနိုင်ပါပြီဗျာ။ 👇"
        )
        bot.send_message(message.chat.id, group_text, parse_mode="Markdown", reply_markup=inline_markup)

# =========================================================
# 🎛️ Inline Button (PASSWORD ရယူရန်) ကို နှိပ်ခဲ့လျှင်
# =========================================================
@bot.callback_query_handler(func=lambda call: call.data == "get_password_now")
def callback_inline(call):
    user_id = call.message.chat.id
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
    
    bot.send_message(user_id, info_text, parse_mode="Markdown", reply_markup=inline_markup)
    bot.answer_callback_query(call.id)

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
        
