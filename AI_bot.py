from openai import OpenAI
import telebot

token = '8146333746:AAFw-Jj-BghNwORJ5PUQg8bPFEwMtcDoTGg'
bot = telebot.TeleBot(token)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! \n"
                          "Я твой искусственный ассистент. Что сегодня ты хочешь узнать? \n"
                          "Чтобы задать вопрос следуй инструкции: /tell <вопрос>")

@bot.message_handler(commands=['tell'])
def tell(message):
    question = message.text.split(' ', 1)[1]
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "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", # Optional. Site URL for rankings on openrouter.ai.
            "X-Title": "Tg_Bot",  # Optional. Site title for rankings on openrouter.ai.
        },
        extra_body={},
        model="nousresearch/deephermes-3-mistral-24b-preview:free",
        messages=[
          {
            "role": "user",
            "content": f"{question}"
          }
        ]
    )
    bot.reply_to(message, completion.choices[0].message.content)

bot.polling(none_stop=True)

