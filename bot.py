import telebot
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🔥 USMLE MODE ACTIVATED 🔥\nاكتب /plan لرؤية خطة اليوم")

@bot.message_handler(commands=['plan'])
def send_plan(message):
    bot.reply_to(message, "📚 خطة اليوم:\n1- Cell Injury\n2- Necrosis\n3- 20 MCQs")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "تم الاستلام ✅")

bot.infinity_polling()