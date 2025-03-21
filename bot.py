import telebot

# تنظیمات ربات
TOKEN = "7839479979:AAH8itSpDMSYouszf9-0-RrRKXNQg_QKLww"  # توکن شما جایگزین شد
CHANNEL = "@Shortvideos553"  # آیدی کانال شما جایگزین شد

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    bot.reply_to(message, f"سلام! برای دریافت توکن، عضو کانال {CHANNEL} شوید!")

bot.polling()
