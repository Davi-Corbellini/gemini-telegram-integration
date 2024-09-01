import telebot
import google.generativeai as genai

GOOGLE_API_KEY="SUA_CHAVE_GOOGLE"
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "candidate_count": 1,
    "temperature": 0.5
}

safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE"

}

model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings )

CHAVE_API = "SUA_CHAVE_TELEGRAM"

bot = telebot.TeleBot(CHAVE_API)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    response = model.generate_content(mensagem.text)
    bot.reply_to(mensagem, response.text)

bot.polling()



