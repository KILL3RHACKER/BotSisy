import telebot
from telebot import types

# Замените <YOUR_BOT_TOKEN> на токен вашего бота, полученный у @BotFather
bot = telebot.TeleBot("7035089963:AAFY-cXzP2-ZsL_Kv6ddC6kgMljx1DgjhsY")

bot.set_my_commands([
    types.BotCommand("goyda", "Сказать ГОООООЙДААА!!!"),
    types.BotCommand("venom", "Отправить фото Венома"),
    types.BotCommand("dvorf", "Отправить фотку Дворфа"),
])

# Обработчик команды /goyda
@bot.message_handler(commands=['goyda'])
def handle_goyda(message):
    bot.reply_to(message, "ГОООООЙДААА!!!")
    
@bot.message_handler(commands=['venom'])
def handle_venom(message):
    photo_url = "https://i.ytimg.com/vi/V5ETbCNO79U/maxresdefault.jpg"
    bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption="Venom!")
    
@bot.message_handler(commands=['dvorf'])
def handle_dvorf(message):
    # Ссылка на вашу чёрно-белую фотографию
    # Если у вас нет прямой URL, нужно сначала загрузить фото куда-то в Интернет
    photo_url = "https://imgur.com/a/vtQjLNl"
    bot.send_photo(chat_id=message.chat.id, photo=photo_url)

if __name__ == '__main__':
    bot.polling()