from telebot import TeleBot
 
bot = TeleBot('8067613966:AAEypFQHXUiVc7WHAKXlWtETV_mSutl7Rec')
 
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Йоу, напиши мне */день недели*, \n а я переведу его на английский', parse_mode='Markdown')
    
@bot.message_handler(commands=['понедельник'])
def transmon(message):
    bot.send_message(message.chat.id, 'monday', parse_mode='Markdown')    

@bot.message_handler(commands=['вторник'])
def transtue(message):
    bot.send_message(message.chat.id, 'tuesday', parse_mode='Markdown')
    
@bot.message_handler(commands=['среда'])
def transwed(message):
    bot.send_message(message.chat.id, 'wednesday', parse_mode='Markdown')
    
@bot.message_handler(commands=['четверг'])
def transthu(message):
    bot.send_message(message.chat.id, 'thursday', parse_mode='Markdown')
 
@bot.message_handler(commands=['пятницв'])
def transfri(message):
    bot.send_message(message.chat.id, 'friday', parse_mode='Markdown')
    
@bot.message_handler(commands=['суббота'])
def transsat(message):
    bot.send_message(message.chat.id, 'saturday', parse_mode='Markdown')
    
@bot.message_handler(commands=['воскресенье'])
def transsun(message):
    bot.send_message(message.chat.id, 'sunday', parse_mode='Markdown')
    
bot.infinity_polling()