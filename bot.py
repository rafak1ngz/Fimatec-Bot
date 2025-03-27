import telebot
import os

# Pegamos o token do bot no ambiente
TOKEN = os.getenv("7846920885:AAEDv34yHHXtlhpWQisBWwwxESp2LY998kM")
bot = telebot.TeleBot(TOKEN)

# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Eu sou o FimatecBot. Como posso te ajudar hoje?")

# Responde qualquer mensagem
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Você disse: {message.text}")

# Inicia o bot
if __name__ == "__main__":
    print("Bot está rodando...")
    bot.polling()

# Inicio do arquivo