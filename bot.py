import telebot
import os

# Pegamos o token do bot no ambiente
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    print("Erro: TELEGRAM_BOT_TOKEN não encontrado.")
    exit(1)  # Encerra o programa se o token não estiver definido

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
    try:
        print("Bot está rodando...")
        bot.polling()
    except Exception as e:
        print(f"Erro ao rodar o bot: {e}")
